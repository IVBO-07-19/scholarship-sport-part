from rest_framework.views import APIView

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


def permission_allowed(head, permission):
    user_roles = requests.get(url=service_URL + f'users/roles/', headers=head).json()
    allowed = False
    for role in user_roles:
        allowed = allowed or role.get('position') == permission
    return allowed


def change(request, serializer, token, type, id):
    user_id = jwt_decode_token(token).get('sub')
    data = serializer(data=request.data).initial_data
    record = type.objects.get(pk=id)
    request_id = record.requestID
    head = {'Authorization': f'Bearer {token}'}
    req_info = requests.get(url=service_URL + f'application/get/{request_id}/', headers=head).json()
    if req_info == 'Application does not exist':
        return JsonResponse(get_update_details('not_exist'), status=status.HTTP_200_OK, safe=False)
    req_ready = req_info.get('readystatus').get('status')
    if not req_ready:
        return JsonResponse(get_update_details('is_ready'), status=status.HTTP_200_OK, safe=False)
    if permission_allowed(head, 'student') and record.userID == user_id:
        if data.keys().__contains__('points'):
            data = data.copy()
            data.pop('points')
        for fld in data.keys():
            setattr(record, fld, data.get(fld))
    elif permission_allowed(head, 'director'):
        record.points = data.get('points')
    ser_data = serializer(data=record.__dict__)
    if ser_data.is_valid():
        record.save()
        return JsonResponse(ser_data.data, safe=False)
    return JsonResponse(get_update_details('not_allowed'), status=status.HTTP_403_FORBIDDEN, safe=False)

# --- POST --- #
def add(serialized, token, serializer):
    if serialized.is_valid():
        user_id = jwt_decode_token(token).get('sub')
        data = serialized.data
        request_id = data.get('requestID')
        head = {'Authorization': f'Bearer {token}'}
        # Check request
        req_info = requests.get(url=service_URL + f'application/get/{request_id}/', headers=head).json()
        if req_info == 'Application does not exist':
            return JsonResponse(get_update_details('not_exist'), status=status.HTTP_200_OK, safe=False)

        req_ready = req_info.get('readystatus').get('status')
        if not req_ready:
            return JsonResponse(get_update_details('is_ready'), status=status.HTTP_200_OK, safe=False)

        # Check user
        if not permission_allowed(head, 'student'):
            return JsonResponse(get_update_details('not_allowed'), status=status.HTTP_403_FORBIDDEN, safe=False)

        obj = serialized.to_object()
        obj.userID = user_id
        obj.points = 0
        obj.save()
        return JsonResponse(serializer(obj).data, status=status.HTTP_201_CREATED, safe=False)
    return JsonResponse(serialized.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)


class GlobalEventList(generics.ListCreateAPIView):
    http_method_names = ['get', 'post']
    queryset = GlobalEvent.objects.all()
    serializer_class = GlobalEventSerializer

    def post(self, request, *args, **kwargs):
        token = get_token_auth_header(request)
        serialized = GlobalEventSerializer(data=request.data)
        return add(serialized, token, GlobalEventSerializer)


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
        serialized = TRPBadgeSerializer(data=request.data)
        return add(serialized, token, TRPBadgeSerializer)


class TRPBadgeDetail(generics.RetrieveUpdateDestroyAPIView):
    http_method_names = ['get', 'patch', 'delete']
    queryset = TRPBadge.objects.all()
    serializer_class = TRPBadgeSerializer

    def patch(self, request, *args, **kwargs):
        token = get_token_auth_header(request)
        serialized = TRPBadgeSerializer(data=request.data)
        return change(request, self.serializer_class, token, GlobalEvent, self.kwargs['pk'])


class NationalPartList(generics.ListCreateAPIView):
    http_method_names = ['get', 'post']
    queryset = NationalPart.objects.all()
    serializer_class = NationalPartSerializer

    def post(self, request, *args, **kwargs):
        token = get_token_auth_header(request)
        serialized = NationalPartSerializer(data=request.data)
        return add(serialized, token, NationalPartSerializer)


class NationalPartDetail(generics.RetrieveUpdateDestroyAPIView):
    http_method_names = ['get', 'patch', 'delete']
    queryset = NationalPart.objects.all()
    serializer_class = NationalPartSerializer

    def patch(self, request, *args, **kwargs):
        token = get_token_auth_header(request)
        serialized = NationalPartSerializer(data=request.data)
        return change(request, self.serializer_class, token, GlobalEvent, self.kwargs['pk'])


class NotNationalPartList(generics.ListCreateAPIView):
    http_method_names = ['get', 'post']
    queryset = NotNationalPart.objects.all()
    serializer_class = NotNationalPartSerializer

    def post(self, request, *args, **kwargs):
        token = get_token_auth_header(request)
        serialized = NotNationalPartSerializer(data=request.data)
        return add(serialized, token, NotNationalPartSerializer)


class NotNationalPartDetail(generics.ListCreateAPIView):
    http_method_names = ['get', 'patch', 'delete']
    queryset = NotNationalPart.objects.all()
    serializer_class = NotNationalPartSerializer

    def patch(self, request, *args, **kwargs):
        token = get_token_auth_header(request)
        serialized = NotNationalPartSerializer(data=request.data)
        return change(request, self.serializer_class, token, GlobalEvent, self.kwargs['pk'])


class OnlineDetail(generics.RetrieveUpdateDestroyAPIView):
    http_method_names = ['get', 'patch', 'delete']
    queryset = Online.objects.all()
    serializer_class = OnlineSerializer

    def patch(self, request, *args, **kwargs):
        token = get_token_auth_header(request)
        serialized = OnlineSerializer(data=request.data)
        return change(request, self.serializer_class, token, GlobalEvent, self.kwargs['pk'])


class OnlineList(generics.ListCreateAPIView):
    http_method_names = ['get', 'post']
    queryset = Online.objects.all()
    serializer_class = OnlineSerializer

    def post(self, request, *args, **kwargs):
        token = get_token_auth_header(request)
        serialized = OnlineSerializer(data=request.data)
        return add(serialized, token, OnlineSerializer)


class RequestList(APIView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        request_id = self.kwargs['id']
        global_events = GlobalEvent.objects.filter(requestID=request_id).values('name', 'level', 'degree', 'place',
                                                                                'date', 'points')
        trp_badges = TRPBadge.objects.filter(requestID=request_id).values('trp_badge', 'date', 'age_group', 'points')
        national_part = NationalPart.objects.filter(requestID=request_id).values('name', 'degree', 'date', 'points')
        not_national_part = NotNationalPart.objects.filter(requestID=request_id).values('name', 'level', 'degree',
                                                                                        'date', 'points')
        online = Online.objects.filter(requestID=request_id).values('name', 'date', 'points')
        response = {
            '1': list(global_events),
            '2': list(trp_badges),
            '3.1': list(national_part),
            '3.2': list(not_national_part),
            '3.3': list(online)
        }
        return JsonResponse(response, safe=False)
