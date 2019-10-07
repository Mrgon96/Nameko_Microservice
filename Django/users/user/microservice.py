import json
import django
import os
from django.conf import settings
from nameko import rpc
# from nameko.rpc import rpc
# from ..user.models import Students
from .models import Students
from .serializers import StudentSerializer
# from ..user.serializers import StudentSerializer
from django.contrib.auth.models import User
from django.core import serializers
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "../users/setiings")
django.setup()


# class Service:
#     @rpc
#     def method():
#         return SomeModel.objects.all().count()





class StudentService:
    name = "student_service"

    @rpc
    def get(self):
        students = Students.objects.all()
        ser = StudentSerializer(students, many=True)
        # user = User.objects.all()
        # json_data = serializers.serialize(user)
        return ser.data











