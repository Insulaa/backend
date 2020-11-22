from django.shortcuts import render
from patients.models import Users, User_Setup, Medication
from rest_framework import viewsets, permissions, generics
from .serializers import UserSerializer, SetupSerializer, MedicationSerializer
from django_filters.rest_framework import DjangoFilterBackend

#User ViewSet

class UserViewSet(viewsets.ModelViewSet):

    queryset = Users.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
    # filter_backends = (DjangoFilterBackend)
    filterset_fields = ['user_id', 'first_name']

class SetupViewSet(viewsets.ModelViewSet):

    queryset = User_Setup.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SetupSerializer

class MedicationViewSet(viewsets.ModelViewSet):

    queryset = Medication.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MedicationSerializer