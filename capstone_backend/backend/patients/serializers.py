from rest_framework import serializers
from patients.models import Users, User_Setup

# User Serializer 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

