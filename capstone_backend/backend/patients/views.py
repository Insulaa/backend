from django.shortcuts import render
from patients.models import Users, User_Setup, Medication
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, SetupSerializer, MedicationSerializer

#User ViewSet

class UserViewSet(viewsets.ModelViewSet):

    queryset = Users.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

class SetupViewSet(viewsets.ModelViewSet):

    queryset = User_Setup.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SetupSerializer

class MedicationViewSet(viewsets.ModelViewSet):

    queryset = Medication.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MedicationSerializer