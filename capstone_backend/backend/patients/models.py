from django.db import models 

class Medication_master(models.Model):
    medication_id = models.IntegerField(primary_key=True, unique=True)
    medication_name = models.CharField(max_length=500)
    medication_unit = models.CharField(max_length=20)

    class Meta:
        db_table = 'Medication_master'

class Users(models.Model):
    user_id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'Users'

#need to figure out how to do this 
class User_Setup(models.Model):
    user = models.ForeignKey(Users, related_name='user_setup', on_delete=models.CASCADE) 
    question1 = models.CharField(max_length=100)
    question2 = models.CharField(max_length=100)
    question3 = models.CharField(max_length=100)

    class Meta:
        db_table = 'User_Setup'

class Medication(models.Model):
    medication_input_id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(Users, related_name='user_medication', on_delete=models.CASCADE) 
    medication_id = models.ForeignKey(Medication_master, related_name='medication', on_delete=models.CASCADE) 
    # medication_image = models.ImageField(upload_to='images/')
    frequency = models.CharField(max_length=100)
    currently_taking = models.BooleanField(default=0)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Medication'

class Glucose_level(models.Model):
    user = models.ForeignKey(Users, related_name='user_glucose', on_delete=models.CASCADE) 
    glucose_reading = models.IntegerField(blank=True, null=True)
    date = models.DateField(auto_now=True)
    timestamp = models.TimeField(auto_now=True)

class Blood_pressure(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE) 
    bp_reading = models.IntegerField(blank=True, null=True)
    date = models.DateField(auto_now=True)
    timestamp = models.TimeField(auto_now=True)

class Weight(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE) 
    weight_reading = models.IntegerField(blank=True, null=True)
    weight_unit = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    timestamp = models.TimeField(auto_now=True)