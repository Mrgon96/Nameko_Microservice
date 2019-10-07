from django.shortcuts import render

# Create your views here.
from nameko import rpc
# from ..user.models import Students
from .models import Students
from .serializers import StudentSerializer
# from ..user.serializers import StudentSerializer
# from django.contrib.auth.models import User
from django.core import serializers


class StudentService:
    name = "student_service"

    @rpc
    def get(self):
        students = Students.objects.all()
        ser = StudentSerializer(students, many=True)
        # user = User.objects.all()
        # json_data = serializers.serialize(user)
        return ser.data

