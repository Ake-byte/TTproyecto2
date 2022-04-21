from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Registro

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = '__all__'