from rest_framework import serializers
from django.contrib.auth import get_user_model
from patients.models import Medication_master, CustomUser, User_Setup, Medication, Glucose_level, Blood_pressure, Weight

class MedicationMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication_master
        fields = '__all__'
        read_only_fields = ('medication_id', 'medication_name', 'medication_unit')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        write_only_fields = ('password')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = '__all__'
        write_only_fields = ('password')
    
    def create(self, validated_data):
        user = super(RegisterSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class SetupSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User_Setup
        fields = '__all__'

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'

class GlucoseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Glucose_level
        fields = '__all__'
        read_only_fields = ('date', 'timestamp')

class GlucoseFourteenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Glucose_level
        fields = ('date', 'glucose_reading', 'id', 'patient_id', 'timestamp')


class BloodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blood_pressure
        fields = '__all__'

class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = '__all__'