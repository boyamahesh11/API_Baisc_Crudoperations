from django.shortcuts import render

# Create your views here.
from app.models import *
from app.serializers import *

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET','POST','DELETE'])
def employeedata(request):
    EMPDATA=Employee.objects.all()
    EMPJSONDATA=EmployeeModelserializers(EMPDATA,many=True)

    return Response(EMPJSONDATA.data)