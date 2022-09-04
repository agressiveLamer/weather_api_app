from rest_framework import serializers
from .models import *


class FactWetaherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact
        fields = ('temp', 'feels_like', 'icon', 'condition')
        depth = 1


class TimeZoneWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time_zone_info
        fields = ('offset', 'name', 'abbr', 'dst')
        depth = 1


class InfoWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ('lat', 'lon', 'tz', 'def_pressure_mm', 'def_pressure_pa', 'url')
        depth = 1


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ('now', 'now_dt', 'info', 'fact')
