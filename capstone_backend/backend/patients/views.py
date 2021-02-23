from django.shortcuts import render
from patients.models import Patients, Patient_Setup, Medication, Glucose_level, Medication_master
from rest_framework import viewsets, permissions, generics, status 
from .serializers import PatientSerializer, SetupSerializer, MedicationSerializer, GlucoseSerializer, MedicationMasterSerializer
from django_filters.rest_framework import DjangoFilterBackend
import datetime 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.db.models import Avg, Count, Sum

class MedicationMasterViewSet(viewsets.ModelViewSet):

    queryset = Medication_master.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MedicationMasterSerializer

class PatientViewSet(viewsets.ModelViewSet):

    queryset = Patients.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PatientSerializer
    # filter_backends = (DjangoFilterBackend)
    filterset_fields = ['patient_id', 'first_name']

class SetupViewSet(viewsets.ModelViewSet):

    queryset = Patient_Setup.objects.all()
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
    filterset_fields = ['patient_id', 'date']

# class GlucoseFilter(filters.FilterSet):
#     start_date = filters.DateFilter(lookup_expr="gte")
#     end_date = filters.DateFilter(lookup_expr="lte")

#     class Meta:
#         model = Glucose_level
#         fields = [
#             "patient",
#             "glucose_reading",
#             "date",
#             "timestamp",
#             "start_date",
#             "end_date",
#         ]

class FourteenDayAvg(viewsets.ModelViewSet):

    serializer_class = GlucoseSerializer

    # @action(method=['get'], permission_classes=[AllowAny])
    def get_queryset(self):

        patient_id = self.request.query_params.get('patient_id')
        sdate = (datetime.date.today() - datetime.timedelta(days=14)).strftime('%Y-%m-%d')
        edate = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        patient_list = Glucose_level.objects.filter(date__range =(sdate,edate), patient_id=patient_id)
        # final = patient_list.all().aggregate(Avg('glucose_reading'))
        return patient_list

