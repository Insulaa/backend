from django.db import models 
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from phone_field import PhoneField
from .managers import CustomUserManager
import datetime

class Medication_master(models.Model):
    medication_id = models.IntegerField(primary_key=True, unique=True)
    medication_name = models.CharField(max_length=500)

    class Meta:
        db_table = 'Medication_master'

# class Patients(models.Model):
#     patient_id = models.AutoField(primary_key=True, unique=True)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     email = models.CharField(max_length=100, unique=True)
#     phone_number = PhoneField(blank=True)

#     class Meta:
#         db_table = 'Patients'

class CustomUser(AbstractBaseUser, PermissionsMixin):
    patient_id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = PhoneField(blank=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta: 
        db_table = 'Patients'

#need to figure out how to do this 
class User_Setup(models.Model):
    patient = models.ForeignKey(CustomUser, related_name='patient_setup', on_delete=models.CASCADE) 
    question1 = models.CharField(max_length=100)
    question2 = models.CharField(max_length=100)
    question3 = models.CharField(max_length=100)
    upper_bound = models.FloatField(null=True)
    lower_bound = models.FloatField(null=True)

    class Meta:
        db_table = 'Patient_Setup'

def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)

class Medication(models.Model):
    medication_input_id = models.AutoField(primary_key=True, unique=True)
    patient = models.ForeignKey(CustomUser, related_name='patient_medication', on_delete=models.CASCADE) 
    medication = models.ForeignKey(Medication_master, related_name='medication', on_delete=models.CASCADE) 
    image = models.ImageField(upload_to=upload_to, max_length=255, blank=True, null=True)
    dosage = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=20, null=True)
    frequency = models.IntegerField(blank=True, null=True)
    frequency_period = models.CharField(max_length=100, null=True)
    currently_taking = models.BooleanField(default=0)
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    notes = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        db_table = 'Medication'

class Glucose_level(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    glucose_reading = models.FloatField(blank=True, null=True)
    date = models.DateField(auto_now=True)
    #datetime.date.today().strftime('%Y-%m-%d')
    timestamp = models.TimeField(auto_now=True)
    #datetime.datetime.now().strftime("%H:%M:%S")
    
class Blood_pressure(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    bp_reading = models.IntegerField(blank=True, null=True)
    date = models.DateField(auto_now=True)
    timestamp = models.TimeField(auto_now=True)

class Weight(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    weight_reading = models.IntegerField(blank=True, null=True)
    weight_unit = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    timestamp = models.TimeField(auto_now=True)


