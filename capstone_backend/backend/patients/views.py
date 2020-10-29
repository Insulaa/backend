from django.shortcuts import render
from patients.models import Users
from rest_framework import viewsets, permissions
from .serializers import UserSerializer

#User ViewSet

class UserViewSet(viewsets.ModelViewSet):

    queryset = Users.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
