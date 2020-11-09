# from django.db import models
from djongo import models 
# from djongo.models import forms 

class Users(models.Model):
    user_id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)

#need to figure out how to do this 
class User_Setup(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    question1 = models.CharField(max_length=100)
    question2 = models.CharField(max_length=100)
    question3 = models.CharField(max_length=100)

class Medication(models.Model):
    medication_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    prescribed_by = models.CharField(max_length=100)
    dosage = models.IntegerField(blank=True, null=True)  #are we taking this in as an int
    dosage_unit = models.CharField(max_length=50)
    frequency = models.CharField(max_length=100)
    currently_taking = models.BooleanField(default=0)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)

class User_health_metric(models.Model): 
    ""

class Glucose_level(models.Model):
    glucose_reading = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

class Blood_pressure(models.Model):
    bp_reading = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

class Weight(models.Model):
    weight_reading = models.IntegerField(blank=True, null=True)
    weight_unit = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)

