from .serializers import *
from .models import *
from rest_framework import generics, status
from functools import wraps
from .utils import *

from django.http import JsonResponse, HttpResponse

service_URL = 'https://secure-gorge-99048.herokuapp.com/api/'


# --- Authorization methods --- #
def get_token_auth_header(request):
    auth = request.META.get("HTTP_AUTHORIZATION", None)
    parts = auth.split()
    token = parts[1]

    return token


def requires_scope(required_scope):
    def require_scope(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = get_token_auth_header(args[0])
            decoded = jwt.decode(token, verify=False)
            if decoded.get("scope"):
                token_scopes = decoded["scope"].split()
                for token_scope in token_scopes:
                    if token_scope == required_scope:
                        return f(*args, **kwargs)
            response = JsonResponse({'message': 'You don\'t have access to this resource'})
            response.status_code = 403
            return response

        return decorated

    return require_scope


def permission_allowed(head, userID, permission):
    user_roles = requests.get(url=service_URL + f'users/roles/', headers=head).json()
    allowed = False
    for role in user_roles:
        allowed = allowed or role.get('position') == permission
    return allowed


def change(request, serializer, token, type, id):
    user_id = jwt_decode_token(token).get('sub')
    data = serializer(data=request.data).initial_data
    request_id = data.get('requestID')
    head = {'Authorization': f'Bearer {token}'}

    req_info = requests.get(url=service_URL + f'application/get/{request_id}/', headers=head).json()
    if req_info == 'Application does not exist':
        return HttpResponse('Application does not exist', status=status.HTTP_400_BAD_REQUEST)
    req_ready = req_info.get('readystatus').get('status')
    if req_ready:
        return JsonResponse("Application is ready", safe=False)

    if permission_allowed(head, user_id, 'student'):
        if data.keys().__contains__('points'):
            data.pop('points')
        record = type.objects.filter(id=id).update(data)
        return JsonResponse('Changed',safe=False)
    elif permission_allowed(head, user_id, 'director'):
        record = type.objects.filter(id=id)
        record.update(points=data.get('points'))
        return JsonResponse("Changed", safe=False)
    return HttpResponse('Permission denied',status=status.HTTP_400_BAD_REQUEST)


# --- POST --- #
def add(serialized, token, type):
    if serialized.is_valid():
        user_id = jwt_decode_token(token).get('sub')
        data = serialized.data
        request_id = data.get('requestID')
        head = {'Authorization': f'Bearer {token}'}
        # Check request
        req_info = requests.get(url=service_URL + f'application/get/{request_id}/', headers=head).json()
        if req_info == 'Application does not exist':
            return HttpResponse('Application does not exist', status=status.HTTP_400_BAD_REQUEST)
        req_ready = req_info.get('readystatus').get('status')
        if req_ready:
            return JsonResponse("Application is ready", safe=False)

        # Check user
        if not permission_allowed(head, user_id, 'student'):
            return HttpResponse("Permission denied!", status=status.HTTP_400_BAD_REQUEST)

        obj = serialized.to_object()
        obj.userID = user_id
        obj.points = 0
        obj.save()
    return JsonResponse(serialized.errors, safe=False)


class GlobalEventList(generics.ListCreateAPIView):
    http_method_names = ['get', 'post']
    queryset = GlobalEvent.objects.all()
    serializer_class = GlobalEventSerializer

    def post(self, request, *args, **kwargs):
        token = get_token_auth_header(request)
        serialized = GlobalEventSerializer(data=request.data)
        return add(serialized, token, GlobalEvent)


class GlobalEventDetail(generics.RetrieveUpdateDestroyAPIView):
    http_method_names = ['get', 'patch', 'delete']
    queryset = GlobalEvent.objects.all()
    serializer_class = GlobalEventSerializer

    def patch(self, request, *args, **kwargs):
        token = get_token_auth_header(request)
        serialized = GlobalEventSerializer(data=request.data)
        return change(request, self.serializer_class, token, GlobalEvent, self.kwargs['pk'])


class TRPBadgeList(generics.ListCreateAPIView):
    http_method_names = ['get', 'post']
    queryset = TRPBadge.objects.all()
    serializer_class = TRPBadgeSerializer

    def post(self, request, *args, **kwargs):
        token = get_token_auth_header(request)
        serialized = GlobalEventSerializer(data=request.data)
        return add(serialized, token, TRPBadgeList)


class TRPBadgeDetail(generics.RetrieveUpdateDestroyAPIView):
    http_method_names = ['get', 'patch', 'delete']
    queryset = TRPBadge.objects.all()
    serializer_class = TRPBadgeSerializer

    def patch(self, request, *args, **kwargs):
        token = get_token_auth_header(request)
        serialized = GlobalEventSerializer(data=request.data)
        return change(request, self.serializer_class, token, GlobalEvent, self.kwargs['pk'])


class NationalPartList(generics.ListCreateAPIView):
    http_method_names = ['get', 'post']
    queryset = NationalPart.objects.all()
    serializer_class = NationalPartSerializer

    def post(self, request, *args, **kwargs):
        token = get_token_auth_header(request)
        serialized = GlobalEventSerializer(data=request.data)
        return add(serialized, token, NationalPartList)


class NationalPartDetail(generics.RetrieveUpdateDestroyAPIView):
    http_method_names = ['get', 'patch', 'delete']
    queryset = NationalPart.objects.all()
    serializer_class = NationalPartSerializer

    def patch(self, request, *args, **kwargs):
        token = get_token_auth_header(request)
        serialized = GlobalEventSerializer(data=request.data)
        return change(request, self.serializer_class, token, GlobalEvent, self.kwargs['pk'])


class NotNationalPartList(generics.ListCreateAPIView):
    http_method_names = ['get', 'post']
    queryset = NotNationalPart.objects.all()
    serializer_class = NotNationalPartSerializer

    def post(self, request, *args, **kwargs):
        token = get_token_auth_header(request)
        serialized = GlobalEventSerializer(data=request.data)
        return add(serialized, token, NotNationalPartList)


class NotNationalPartDetail(generics.ListCreateAPIView):
    http_method_names = ['get', 'patch', 'delete']
    queryset = NotNationalPart.objects.all()
    serializer_class = NotNationalPartSerializer

class OnlineDetail(generics.RetrieveUpdateDestroyAPIView):
    http_method_names = ['get', 'patch', 'delete']
    queryset = Online.objects.all()
    serializer_class = OnlineSerializer

    def patch(self, request, *args, **kwargs):
        token = get_token_auth_header(request)
        serialized = GlobalEventSerializer(data=request.data)
        return change(request, self.serializer_class, token, GlobalEvent, self.kwargs['pk'])


class OnlineList(generics.ListCreateAPIView):
    http_method_names = ['get', 'post']
    queryset = Online.objects.all()
    serializer_class = OnlineSerializer

    def post(self, request, *args, **kwargs):
        token = get_token_auth_header(request)
        serialized = GlobalEventSerializer(data=request.data)
        return add(serialized, token, OnlineList)
