from django.shortcuts import render
from patients.models import Users, User_Setup, Medication, Glucose_level, Medication_master
from rest_framework import viewsets, permissions, generics, status 
from .serializers import UserSerializer, SetupSerializer, MedicationSerializer, GlucoseSerializer, MedicationMasterSerializer
from django_filters.rest_framework import DjangoFilterBackend
import datetime 
from rest_framework.decorators import api_view

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
def FourteenDayAvg(request):
    if request.method == 'GET':
        startdate = date.today() - datetime.timedelta(days=14)
        enddate = date.today()
        user_id = request.query_params('user_id')
        result=Glucose_level.objects.raw('select ')
    
        
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization