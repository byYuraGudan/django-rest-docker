from django.contrib.auth.models import User, Group, Permission
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ("name", "content_type", "codename",)


class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True)

    class Meta:
        model = Group
        fields = ("name", "permissions")
