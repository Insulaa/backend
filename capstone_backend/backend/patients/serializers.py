from rest_framework import serializers
from patients.models import Medication_master, Patients, Patient_Setup, Medication, Glucose_level, Blood_pressure, Weight

class MedicationMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication_master
        fields = '__all__'
        # read_only_fields = ('medication_id', 'medication_name', 'medication_unit')

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'

class SetupSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Patient_Setup
        fields = '__all__'

class GetMedicationSerializer(serializers.ModelSerializer):
    medication = MedicationMasterSerializer(read_only=True)
    
    class Meta:
        model = Medication
        fields = [
                 'medication_input_id', 
                 'patient',
                 'medication',
                 'image',
                 'dosage',
                 'unit',
                 'frequency',
                 'frequency_period',
                 'currently_taking',
                 'start',
                 'end' 
            ]

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