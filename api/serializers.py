from rest_framework import serializers
from .models import *


class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = '__all__'


class Table1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Table1
        fields = '__all__'
