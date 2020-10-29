from django.db import models

class Users(models.Model):
    user_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)

class User_Setup(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    question1 = models.CharField(max_length=100)

