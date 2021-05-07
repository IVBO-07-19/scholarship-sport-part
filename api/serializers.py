from rest_framework import serializers
from .models import *


class GlobalEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalEvent
        fields = '__all__'

    def to_object(self):
        request_id = self.data.get('requestID')
        name = self.data.get('name')
        level = self.data.get('level')
        degree = self.data.get('degree')
        place = self.data.get('place')
        date = self.data.get('date')
        return GlobalEvent(requestID=request_id, name=name, level=level, degree=degree, place=place, date=date)


class TRPBadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TRPBadge
        fields = '__all__'

    def to_object(self):
        request_id = self.data.get('requestID')
        trp_badge = self.data.get('trp_badge')
        age_group = self.data.get('age_group')
        points = self.data.get('points')
        date = self.data.get('date')
        return GlobalEvent(requestID=request_id, trp_badge=trp_badge, age_group=age_group, points=points, date=date)


class NationalPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = NationalPart
        fields = '__all__'

    def to_object(self):
        request_id = self.data.get('requestID')
        name = self.data.get('name')
        degree = self.data.get('degree')
        points = self.data.get('points')
        date = self.data.get('date')
        return GlobalEvent(requestID=request_id, name=name, degree=degree, points=points, date=date)


class NotNationalPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotNationalPart
        fields = '__all__'

    def to_object(self):
        request_id = self.data.get('requestID')
        name = self.data.get('name')
        level = self.data.get('level')
        degree = self.data.get('degree')
        place = self.data.get('place')
        date = self.data.get('date')
        return GlobalEvent(requestID=request_id, name=name, level=level, degree=degree, place=place, date=date)


class OnlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Online
        fields = '__all__'

    def to_object(self):
        request_id = self.data.get('requestID')
        name = self.data.get('name')
        date = self.data.get('date')
        points = self.data.get('points')
        return GlobalEvent(requestID=request_id, name=name, date=date, points=points)
