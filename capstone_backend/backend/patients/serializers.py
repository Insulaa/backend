from rest_framework import serializers
from patients.models import Medication_master, Patients, Patient_Setup, Medication, Glucose_level, Blood_pressure, Weight

class MedicationMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication_master
        fields = '__all__'
        read_only_fields = ('medication_id', 'medication_name', 'medication_unit')

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'

class SetupSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Patient_Setup
        fields = '__all__'

class MedicationSerializer(serializers.ModelSerializer):
    medication = MedicationMasterSerializer(many=True)
    
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

    def get(self, validated_data):
        medication = validated_data.pop('medication')
        med = Medication.objects.get(**validated_data)
        for m in medication:
            SbQuoteLoccvg.objects.create(**m, med = med)
        return med 
   

#SbQuote Serializer 
# class SbQuoteSerializer(serializers.ModelSerializer):
#     pods = SbQuoteLoccvgSerializer(many=True)

#     class Meta:
#         model = SbQuote
#         fields = [
#             'quote_id', 
#             'quote_name', 
#             'quote_datetime',
#             'quote_optype',
#             'quote_flowtype',
#             'quote_totsowhead',
#             'quote_totmarkethead',
#             'pods'
#         ]

#     def create(self, validated_data):
#         pods = validated_data.pop('pods')
#         quote = SbQuote.objects.create(**validated_data)
#         for pod in pods:
#             SbQuoteLoccvg.objects.create(**pod, quote = quote)
#         return quote 

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