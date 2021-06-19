from django.db.models import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class userseializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['username','password']
class departserializers(serializers.ModelSerializer):
    class Meta:
        model=department
        fields='__all__'
class employserializers(serializers.ModelSerializer):
    class Meta:
        model=employee
        fields='__all__'
