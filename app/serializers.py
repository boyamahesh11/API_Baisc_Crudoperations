from rest_framework import serializers
from app.models import *

class EmployeeModelserializers(serializers.ModelSerializer):
    class Meta:
        model=Employee
        #fields=['Ename','Esal']
        fields='__all__'
        