from django.db import models 
from phone_field import PhoneField
import datetime

class Medication_master(models.Model):
    medication_id = models.IntegerField(primary_key=True, unique=True)
    medication_name = models.CharField(max_length=500)
    medication_unit = models.CharField(max_length=20)

    class Meta:
        db_table = 'Medication_master'

class Patients(models.Model):
    patient_id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    phone_number = PhoneField(blank=True)

    class Meta:
        db_table = 'Patients'

#need to figure out how to do this 
class Patient_Setup(models.Model):
    patient = models.ForeignKey(Patients, related_name='patient_setup', on_delete=models.CASCADE) 
    question1 = models.CharField(max_length=100)
    question2 = models.CharField(max_length=100)
    question3 = models.CharField(max_length=100)

    class Meta:
        db_table = 'Patient_Setup'

class Medication(models.Model):
    medication_input_id = models.AutoField(primary_key=True, unique=True)
    patient = models.ForeignKey(Patients, related_name='patient_medication', on_delete=models.CASCADE) 
    medication = models.ForeignKey(Medication_master, related_name='medication', on_delete=models.CASCADE) 
    medication_image = models.ImageField(upload_to='images/%Y/%m/%d/', max_length=255, null=True, blank=True)
    frequency = models.CharField(max_length=100)
    currently_taking = models.BooleanField(default=0)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Medication'

class Glucose_level(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE) 
    glucose_reading = models.FloatField(blank=True, null=True)
    date = models.DateField(default=datetime.date.today().strftime('%Y-%m-%d'))
    timestamp = models.TimeField(default=datetime.datetime.now().strftime("%H:%M:%S"))

class Blood_pressure(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE) 
    bp_reading = models.IntegerField(blank=True, null=True)
    date = models.DateField(auto_now=True)
    timestamp = models.TimeField(auto_now=True)

class Weight(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE) 
    weight_reading = models.IntegerField(blank=True, null=True)
    weight_unit = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    timestamp = models.TimeField(auto_now=True)