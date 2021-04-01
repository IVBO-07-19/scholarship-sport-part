from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework.decorators import api_view


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
