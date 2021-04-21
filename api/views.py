from django.contrib.auth.decorators import login_required
from rest_framework.decorators import permission_classes
from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from functools import wraps
import jwt

from django.http import JsonResponse


def get_token_auth_header(request):
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.META.get("HTTP_AUTHORIZATION", None)
    parts = auth.split()
    token = parts[1]

    return token


def requires_scope(required_scope):
    """Determines if the required scope is present in the Access Token
    Args:
        required_scope (str): The scope required to access the resource
    """

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


class GlobalEventDetail(generics.RetrieveUpdateDestroyAPIView):
    http_method_names = ['get', 'patch', 'delete']
    queryset = GlobalEvent.objects.all()
    serializer_class = GlobalEventSerializer


class TRPBadgeList(generics.ListCreateAPIView):
    http_method_names = ['get', 'post']
    queryset = TRPBadge.objects.all()
    serializer_class = TRPBadgeSerializer


class TRPBadgeDetail(generics.RetrieveUpdateDestroyAPIView):
    http_method_names = ['get', 'patch', 'delete']
    queryset = TRPBadge.objects.all()
    serializer_class = TRPBadgeSerializer


class NationalPartList(generics.ListCreateAPIView):
    http_method_names = ['get', 'post']
    queryset = NationalPart.objects.all()
    serializer_class = NationalPartSerializer


class NationalPartDetail(generics.RetrieveUpdateDestroyAPIView):
    http_method_names = ['get', 'patch', 'delete']
    queryset = NationalPart.objects.all()
    serializer_class = NationalPartSerializer


class NotNationalPartList(generics.ListCreateAPIView):
    http_method_names = ['get', 'post']
    queryset = NotNationalPart.objects.all()
    serializer_class = NotNationalPartSerializer


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
