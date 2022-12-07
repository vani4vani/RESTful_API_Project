from rest_framework import serializers
from weatherApp.models import WeatherData


class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = '__all__' 