# Generated by Django 3.0.5 on 2021-03-31 19:56

from django.db import migrations, models
import django.db.models.deletion
import patients.models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medication_master',
            fields=[
                ('medication_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('medication_name', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'Medication_master',
            },
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('patient_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('phone_number', phone_field.models.PhoneField(blank=True, max_length=31)),
            ],
            options={
                'db_table': 'Patients',
            },
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight_reading', models.IntegerField(blank=True, null=True)),
                ('weight_unit', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now=True)),
                ('timestamp', models.TimeField(auto_now=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Patients')),
            ],
        ),
        migrations.CreateModel(
            name='Patient_Setup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfBirth', models.DateField(blank=True, null=True)),
                ('sex', models.CharField(max_length=20, null=True)),
                ('height1', models.IntegerField(null=True)),
                ('height1_unit', models.CharField(max_length=20, null=True)),
                ('height2', models.IntegerField(null=True)),
                ('height2_unit', models.CharField(max_length=20, null=True)),
                ('weight', models.IntegerField(null=True)),
                ('weight_unit', models.CharField(max_length=20, null=True)),
                ('glucose_lower_limit', models.FloatField(null=True)),
                ('glucose_upper_limit', models.FloatField(null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_setup', to='patients.Patients')),
            ],
            options={
                'db_table': 'Patient_Setup',
            },
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('medication_input_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to=patients.models.upload_to)),
                ('dosage', models.IntegerField(blank=True, null=True)),
                ('unit', models.CharField(max_length=20, null=True)),
                ('frequency', models.IntegerField(blank=True, null=True)),
                ('frequency_period', models.CharField(max_length=100, null=True)),
                ('currently_taking', models.BooleanField(default=0)),
                ('start', models.DateField(blank=True, null=True)),
                ('end', models.DateField(blank=True, null=True)),
                ('notes', models.CharField(blank=True, max_length=500, null=True)),
                ('medication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medication', to='patients.Medication_master')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_medication', to='patients.Patients')),
            ],
            options={
                'db_table': 'Medication',
            },
        ),
        migrations.CreateModel(
            name='Glucose_level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('glucose_reading', models.FloatField(blank=True, null=True)),
                ('date', models.DateField(auto_now=True)),
                ('timestamp', models.TimeField(auto_now=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Patients')),
            ],
        ),
        migrations.CreateModel(
            name='Blood_pressure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bp_reading', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(auto_now=True)),
                ('timestamp', models.TimeField(auto_now=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Patients')),
            ],
        ),
    ]
