# Generated by Django 3.0.5 on 2021-03-20 07:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('patients', '0008_auto_20210304_0223'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='patients',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='patients',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='patients',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='patients',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='glucose_level',
            name='date',
            field=models.DateField(default='2021-03-20'),
        ),
        migrations.AlterField(
            model_name='glucose_level',
            name='timestamp',
            field=models.TimeField(default='03:12:13'),
        ),
        migrations.AlterField(
            model_name='patients',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
