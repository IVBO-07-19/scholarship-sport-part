from rest_framework import serializers
from .models import *


class GlobalEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalEvent
        fields = '__all__'


class TRPBadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TRPBadge
        fields = '__all__'


class NationalPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = NationalPart
        fields = '__all__'


class NotNationalPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotNationalPart
        fields = '__all__'


class OnlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Online
        fields = '__all__'

