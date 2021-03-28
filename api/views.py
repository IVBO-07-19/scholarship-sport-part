from .serializers import *
from .models import *
from rest_framework import generics


class GlobalEventList(generics.ListCreateAPIView):
    queryset = GlobalEvent.objects.all()
    serializer_class = GlobalEventSerializer


class GlobalEventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GlobalEvent.objects.all()
    serializer_class = GlobalEventSerializer


class TRPBadgeList(generics.ListCreateAPIView):
    queryset = TRPBadge.objects.all()
    serializer_class = TRPBadgeSerializer


class TRPBadgeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TRPBadge.objects.all()
    serializer_class = TRPBadgeSerializer


class NationalPartList(generics.ListCreateAPIView):
    queryset = NationalPart.objects.all()
    serializer_class = NationalPartSerializer


class NationalPartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NationalPart.objects.all()
    serializer_class = NationalPartSerializer


class NotNationalPartList(generics.ListCreateAPIView):
    queryset = NotNationalPart.objects.all()
    serializer_class = NotNationalPartSerializer


class NotNationalPartDetail(generics.ListCreateAPIView):
    queryset = NotNationalPart.objects.all()
    serializer_class = NotNationalPartSerializer


class OnlineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Online.objects.all()
    serializer_class = OnlineSerializer


class OnlineList(generics.ListCreateAPIView):
    queryset = Online.objects.all()
    serializer_class = OnlineSerializer
