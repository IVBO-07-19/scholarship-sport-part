from rest_framework import serializers
from .models import *


class GlobalEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalEvent
        fields = '__all__'
