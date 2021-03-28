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


