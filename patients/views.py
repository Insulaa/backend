from django.shortcuts import render
from django.contrib.auth import get_user_model, login
from patients.models import CustomUser, User_Setup, Medication, Glucose_level, Medication_master, Blood_pressure, Weight
from rest_framework import viewsets, permissions, mixins, generics, status

from report.report_util import glucose_graph, PDFReport
from .serializers import LoginSerializer, UserSerializer, SetupSerializer, RegisterSerializer, GetMedicationSerializer, MedicationSerializer, GlucoseSerializer, GlucoseFourteenSerializer, MedicationMasterSerializer, BloodSerializer
from django_filters.rest_framework import DjangoFilterBackend
import datetime
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer, BaseRenderer
from django.db.models import Avg, Count, Sum
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from knox.models import AuthToken
import numpy as np
import pandas as pd


class MedicationMasterViewSet(viewsets.ModelViewSet):

    queryset = Medication_master.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MedicationMasterSerializer

class PatientViewSet(viewsets.ModelViewSet):

    queryset = CustomUser.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
    # filter_backends = (DjangoFilterBackend)
    filterset_fields = ['patient_id', 'first_name']

class SetupViewSet(viewsets.ModelViewSet):

    queryset = User_Setup.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SetupSerializer
    filterset_fields = ['patient_id']

    def patch(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        data = request.data 

        instance.patient_id = data['patient']
        instance.dateOfBirth = data['dateOfBirth']
        instance.sex = data['sex']
        instance.height1 = data['height1']
        instance.height2 = data['height2']
        instance.height_unit = data['height_unit ']
        instance.weight = data['weight']
        instance.weight_unit = data['weight_unit']
        instance.glucose_lower_limit = data['glucose_lower_limit']
        instance.glucose_upper_limit = data['glucose_upper_limit']


        instance.save()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        self.perform_update(serializer)

        # serializer = MedicationSerializer(instance, patient=True)

        return Response(serializer.data)

class GetSingleMedication(viewsets.ModelViewSet): 

    serializer_class = MedicationMasterSerializer

    def get_queryset(self):

        medication_id = self.request.query_params.get('medication_id')
        medication_single = Medication_master.objects.filter(medication_id=medication_id)
        return medication_single

class GetMedicationCurrent(viewsets.ModelViewSet):

    serializer_class = GetMedicationSerializer

    def get_queryset(self):

        patient_id = self.request.query_params.get('patient_id')
        medication_list_current = Medication.objects.filter(patient_id=patient_id, currently_taking=True)
        return medication_list_current

class GetMedicationHistorical(viewsets.ModelViewSet):

    serializer_class = GetMedicationSerializer

    def get_queryset(self):

        patient_id = self.request.query_params.get('patient_id')
        medication_list_current = Medication.objects.filter(patient_id=patient_id, currently_taking=False)
        return medication_list_current

class EndMedication(viewsets.ModelViewSet, mixins.UpdateModelMixin):

    serializer_class = MedicationSerializer

    def get_queryset(self):
        medications = Medication.objects.all()
        return medications

    # def partial_update(self, request, pk=None):

    #     instance = self.get_object()
    #     data = request.data

    #     instance.patient_id = data['patient']
    #     instance.medication_id = data['medication']
    #     instance.image = data['image']
    #     instance.dosage = data['dosage']
    #     instance.unit = data['unit']
    #     instance.frequency = data['frequency']
    #     instance.frequency_period = data['frequency_period']
    #     instance.currently_taking = False
    #     instance.start = data['start']
    #     instance.end = datetime.date.today().strftime('%Y-%m-%d')
    #     instance.notes = data['notes']

    #     instance.save()

    #     serializer = MedicationSerializer(instance, partial=True)

    #     return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        data = request.data 

        instance.patient_id = data['patient']
        instance.medication = data['medication']
        instance.image = data['image']
        instance.dosage = data['dosage']
        instance.unit = data['unit']
        instance.frequency = data['frequency']
        instance.frequency_period = data['frequency_period']
        instance.currently_taking = False
        instance.start = data['start']
        instance.end = datetime.date.today().strftime('%Y-%m-%d')
        instance.notes = data['notes']

        instance.save()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        self.perform_update(serializer)

        # serializer = MedicationSerializer(instance, patient=True)

        return Response(serializer.data)


class MedicationViewSet(viewsets.ModelViewSet):

    queryset = Medication.objects.all()
    permission_classes = [permissions.AllowAny]
    # parser_classes = [MultiPartParser, FormParser]
    serializer_class = MedicationSerializer
    filterset_fields = ['medication_input_id', 'patient_id']

    def patch(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        data = request.data 

        instance.patient_id = data['patient']
        instance.medication = data['medication']
        instance.image = data['image']
        instance.dosage = data['dosage']
        instance.unit = data['unit']
        instance.frequency = data['frequency']
        instance.frequency_period = data['frequency_period']
        instance.currently_taking = data['currently_taking']
        instance.start = data['start']
        instance.end = data['end']
        instance.notes = data['notes']

        instance.save()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        self.perform_update(serializer)

        # serializer = MedicationSerializer(instance, patient=True)

        return Response(serializer.data)

class GlucoseLevelViewSet(viewsets.ModelViewSet):

    queryset = Glucose_level.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GlucoseSerializer
    filterset_fields = ['patient_id', 'date']

    # def partial_update(self, request, pk=None):

    #     instance = self.get_object()
    #     data = request.data 

    #     instance.patient_id = data['patient']
    #     instance.glucose_reading = data['glucose_reading']

    #     instance.save()

    #     serializer = GlucoseSerializer(instance, partial=True)

    #     return Response(serializer.data)

class GlucoseToday(viewsets.ModelViewSet):

    serializer_class = GlucoseSerializer

    def get_queryset(self):

        patient_id = self.request.query_params.get('patient_id')
        today = datetime.date.today().strftime('%Y-%m-%d')
        patient_list = Glucose_level.objects.filter(date =today, patient_id=patient_id)
        # final = patient_list.all().aggregate(Avg('glucose_reading'))
        return patient_list

class FourteenDayAvg(viewsets.ModelViewSet):

    serializer_class = GlucoseFourteenSerializer

    # @action(method=['get'], permission_classes=[AllowAny])
    def get_queryset(self):

        patient_id = self.request.query_params.get('patient_id')
        sdate = (datetime.date.today() - datetime.timedelta(days=14)).strftime('%Y-%m-%d')
        edate = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        patient_list = Glucose_level.objects.filter(date__range =(sdate,edate), patient_id=patient_id)
        # .values('glucose_reading')
        
        # final = patient_list.all().aggregate(avg_g = Avg('glucose_reading'))
        # p = patient_list.items()
        # lst = list(patient_list)[0]

        # for each in lst:
        #     a = list()
        #     a.append(each.glucose_reading)

        # avg = sum(a)/len(a)
        return patient_list 

class RegisterUserViewSet(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })
    
class LoginViewSet(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        # serializer = AuthTokenSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # user = serializer.validated_data['user']
        # login(request, user)
        # return super(LoginViewSet, self).post(request, format=None)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class GetUserIdWithTokenViewSet(viewsets.ModelViewSet):
    serializer_class = AuthTokenSerializer

    def get_queryset(self):

        token = self.request.query_params.get('token')
        user_id = knox_authtoken.objects.filter(token = token)
        return user_id


class BloodPressureViewSet(viewsets.ModelViewSet):

    queryset = Blood_pressure.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BloodSerializer
    # filter_backends = (DjangoFilterBackend)
    filterset_fields = ['patient_id']

class BinaryFileRenderer(BaseRenderer):
    media_type = 'application/octet-stream'
    format = None
    charset = None
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return data

class ReportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    @action(methods=['get'], detail=False, renderer_classes=(BinaryFileRenderer,))
    def download(self, request, *args, **kwargs):
        patient_id = self.request.query_params.get('patient_id')
        start_date = (datetime.date.today() - datetime.timedelta(days=14)).strftime('%Y-%m-%d')
        end_date = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')

        glucose_reading = Glucose_level.objects.filter(patient_id=patient_id, date__range =(start_date, end_date)).values_list('glucose_reading', flat=True)
        glucose_reading_date = Glucose_level.objects.filter(patient_id=patient_id, date__range=(start_date, end_date)).values_list('date', flat=True)
        glucose_reading_time = Glucose_level.objects.filter(patient_id=patient_id, date__range=(start_date, end_date)).values_list('timestamp', flat=True)
        glucose_df = pd.DataFrame(np.column_stack([glucose_reading, glucose_reading_date, glucose_reading_time]), columns=['glucose_reading', 'date', 'time'])
        glucose_graph(glucose_df)

        first_name = CustomUser.objects.filter(patient_id=patient_id).values_list('first_name', flat=True)[0]
        last_name = CustomUser.objects.filter(patient_id=patient_id).values_list('last_name', flat=True)[0]

        weight = User_Setup.objects.filter(patient_id=patient_id).values_list('weight', flat=True)[0]

        medications = Medication.objects.filter(patient_id=patient_id).values('medication', 'dosage', 'unit', 'frequency', 'frequency_period', 'currently_taking', 'start', 'end')

        PDFReport("report/Patient_Report.pdf")

        with open('report/Patient_Report.pdf', 'rb') as report:
            return Response(
                report.read(),
                headers={'Content-Disposition': 'attachment; filename="Patient_Report.pdf"'},
                content_type='application/pdf')

