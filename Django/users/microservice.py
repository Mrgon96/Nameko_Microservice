import django
import os
from django.conf import settings

from nameko.rpc import rpc

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "users.settings")
django.setup()
from django.contrib.auth. models import User
from django.contrib.auth import authenticate
from user.models import Students
from user.serializers import StudentSerializer, UserSerializer

class Service:
    name = "http_service"

    @rpc
    def user_list(self):
        users = User.objects.all()
        ser = UserSerializer(users, many=True)
        return ser.data

    @rpc
    def login(self, logindata):
        username = logindata['username']
        password = logindata['password']
        user = authenticate(username=username, password=password)
        if user:
            return user.username
        else:
            return "No user of such Credentials"
    # @rpc
    # def method(self):
    #     students = Students.objects.all()
    #     ser = StudentSerializer(students, many=True)
    #     return ser.data






