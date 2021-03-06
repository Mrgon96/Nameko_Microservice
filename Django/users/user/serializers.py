from rest_framework import serializers
from .models import Students
from django.contrib.auth.models import User


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
