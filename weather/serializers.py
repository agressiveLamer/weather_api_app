from rest_framework import serializers
from .models import *


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'

    def create(self, validated_data):
        return Weather.objects.create(**validated_data)