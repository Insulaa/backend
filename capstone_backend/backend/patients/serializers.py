from rest_framework import serializers
from patients.models import Users, User_Setup, Medication, User_health_metric, Glucose_level, Blood_pressure, Weight
from rest_framework_mongoengine.serializers import DocumentSerializer
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

class GlucoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Glucose_level
        fields = '__all__'

class BloodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blood_pressure
        fields = '__all__'

class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = '__all__'

class HealthMetricSerializer(serializers.ModelSerializer):
    Glucose = GlucoseSerializer(many=True)
    BloodPressure = BloodSerializer(many=True)
    Weight = WeightSerializer(many=True)

    class Meta:
        model = User_health_metric
        fields = ['Glucose',
                 'BloodPressue',
                 'Weight'
        ]

    #FIX UP 

    # def create(self, validated_data):
    #     pods = validated_data.pop('pods')
    #     quote = SbQuote.objects.create(**validated_data)
    #     for pod in pods:
    #         SbQuoteLoccvg.objects.create(**pod, quote = quote)
    #     return quote