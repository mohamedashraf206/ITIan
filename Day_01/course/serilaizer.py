from rest_framework import serializers
from .models import *
from django.db.models import fields


class courses_serializer(serializers.ModelSerializer):
    class Meta:
        model=courses
        fields = '__all__'
