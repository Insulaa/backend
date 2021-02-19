from django.shortcuts import render
from patients.models import Users, User_Setup, Medication, Glucose_level, Medication_master
from rest_framework import viewsets, permissions, generics, status 
from .serializers import UserSerializer, SetupSerializer, MedicationSerializer, GlucoseSerializer, MedicationMasterSerializer
from django_filters.rest_framework import DjangoFilterBackend
import datetime 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

class MedicationMasterViewSet(viewsets.ModelViewSet):

    queryset = Medication_master.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MedicationMasterSerializer

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

class GlucoseLevelViewSet(viewsets.ModelViewSet):

    queryset = Glucose_level.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GlucoseSerializer
    filterset_fields = ['user_id', 'date']

@api_view(['GET'])
# @renderer_classes([JSONRenderer])
@permission_classes([AllowAny])
def FourteenDayAvg(request):
    if request.method == 'GET':
        startdate = (datetime.date.today() - datetime.timedelta(days=14)).strftime("%Y/%M/%D")
        enddate = datetime.date.today().strftime("%Y/%M/%D")
        user_id = request.query_params.get('user_id')
        result = Glucose_level.objects.raw('SELECT AVG(glucose_reading) FROM `capstone-tables`.patients_glucose_level where date BETWEEN ' + startdate + ' AND ' + enddate + ' AND user_id = ' + user_id)   
        
        return render(request, result)