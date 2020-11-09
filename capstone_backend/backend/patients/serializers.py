from rest_framework import serializers
from patients.models import Users, User_Setup, Medication

# User Serializer 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class SetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Setup
        fields = '__all__'

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'
