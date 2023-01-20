from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import wedding_form_001


class wedding_serializer(ModelSerializer):
    class Meta:
        model = wedding_form_001
        fields = ['id', 'wed_001_name_w', 'wed_001_name_m']
