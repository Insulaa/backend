# from django.db import models
from djongo import models 
# from djongo.models import forms 
# from rest_framework_mongoengine.fields import ObjectIdField
import uuid

class Medication_master(models.Model):
    medication_id = models.IntegerField()
    medication_name = models.CharField(max_length=500)

class Users(models.Model):
    user_id = models.UUIDField(default = uuid.uuid4, editable=False, primary_key=True, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)

#need to figure out how to do this 
class User_Setup(models.Model):
    
    question1 = models.CharField(max_length=100)
    question2 = models.CharField(max_length=100)
    question3 = models.CharField(max_length=100)

class Medication(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE) 
    medication_id = models.ForeignKey(Medication_master, on_delete=models.CASCADE) 
    name = models.ForeignKey(Medication_master, on_delete=models.CASCADE)
    prescribed_by = models.CharField(max_length=100)
    dosage_amount = models.IntegerField(blank=True, null=True)  #are we taking this in as an int
    dosage_unit = models.CharField(max_length=50)
    dosage_form = models.CharField(max_length=100)
    #strength 
    frequency = models.CharField(max_length=100)
    currently_taking = models.BooleanField(default=0)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)


class User_health_metric(models.Model): 
    u_id = models.IntegerField(blank=True, null=True)

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

