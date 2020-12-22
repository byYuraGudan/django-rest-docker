from rest_framework import viewsets
from django.contrib.auth import models as auth_models

from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = auth_models.User.objects.all()
    serializer_class = serializers.UserSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = auth_models.Permission.objects.all()
    serializer_class = serializers.PermissionSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = auth_models.Group.objects.all()
    serializer_class = serializers.GroupSerializer
