from rest_framework import serializers
from django.contrib.auth.models import User


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = {
            'firstname',
            'lastname',
            'email',
            'url'
        }