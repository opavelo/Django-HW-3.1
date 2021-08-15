# TODO: опишите сериализаторы

from rest_framework import serializers

from .models import Project, Measurement


class Projectserializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'latitude', 'longitude', 'created_at', 'updated_at']


class Measurementserializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'