from .utils import jwt_get_username_from_payload_handler
from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from functools import wraps
import jwt
from .utils import *

from django.http import JsonResponse, HttpResponse

service_URL = 'https://secure-gorge-99048.herokuapp.com/api/'


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


class GlobalEventList(generics.ListCreateAPIView):
    http_method_names = ['get', 'post']
    queryset = GlobalEvent.objects.all()
    serializer_class = GlobalEventSerializer

    def post(self, request, *args, **kwargs):
        token = get_token_auth_header(request)
        user_id = jwt_decode_token(token).get('sub')
        data = GlobalEventSerializer(request.data).data
        request_id = data.get('requestID')
        head = {'Authorization': f'Bearer {token}'}
        req_status = requests.get(url=service_URL + f'get/{request_id}', headers=head).content
        return HttpResponse(req_status)


class GlobalEventDetail(generics.RetrieveUpdateDestroyAPIView):
    http_method_names = ['get', 'patch', 'delete']
    queryset = GlobalEvent.objects.all()
    serializer_class = GlobalEventSerializer


class TRPBadgeList(generics.ListCreateAPIView):
    http_method_names = ['get', 'post']
    queryset = TRPBadge.objects.all()
    serializer_class = TRPBadgeSerializer

    def post(self, request, *args, **kwargs):
        user_id = jwt_decode_token(get_token_auth_header(request)).get('sub')
        data = GlobalEventSerializer(request.data).data
        request_id = data.get('request_id')

        return JsonResponse(request_id, safe=False)


class TRPBadgeDetail(generics.RetrieveUpdateDestroyAPIView):
    http_method_names = ['get', 'patch', 'delete']
    queryset = TRPBadge.objects.all()
    serializer_class = TRPBadgeSerializer

    def patch(self, request, *args, **kwargs):
        pass


class NationalPartList(generics.ListCreateAPIView):
    http_method_names = ['get', 'post']
    queryset = NationalPart.objects.all()
    serializer_class = NationalPartSerializer

    def post(self, request, *args, **kwargs):
        user_id = jwt_decode_token(get_token_auth_header(request)).get('sub')
        data = GlobalEventSerializer(request.data).data
        request_id = data.get('request_id')
        return JsonResponse(request_id, safe=False)


class NationalPartDetail(generics.RetrieveUpdateDestroyAPIView):
    http_method_names = ['get', 'patch', 'delete']
    queryset = NationalPart.objects.all()
    serializer_class = NationalPartSerializer


class NotNationalPartList(generics.ListCreateAPIView):
    http_method_names = ['get', 'post']
    queryset = NotNationalPart.objects.all()
    serializer_class = NotNationalPartSerializer

    def post(self, request, *args, **kwargs):
        user_id = jwt_decode_token(get_token_auth_header(request)).get('sub')
        data = GlobalEventSerializer(request.data).data
        request_id = data.get('request_id')

        return JsonResponse(request_id, safe=False)


class NotNationalPartDetail(generics.ListCreateAPIView):
    http_method_names = ['get', 'post']
    queryset = NotNationalPart.objects.all()
    serializer_class = NotNationalPartSerializer


class OnlineDetail(generics.RetrieveUpdateDestroyAPIView):
    http_method_names = ['get', 'patch', 'delete']
    queryset = Online.objects.all()
    serializer_class = OnlineSerializer


class OnlineList(generics.ListCreateAPIView):
    http_method_names = ['get', 'patch', 'delete']
    queryset = Online.objects.all()
    serializer_class = OnlineSerializer

    def post(self, request, *args, **kwargs):
        user_id = jwt_decode_token(get_token_auth_header(request)).get('sub')
        data = GlobalEventSerializer(request.data).data
        request_id = data.get('request_id')

        return JsonResponse(request_id, safe=False)
