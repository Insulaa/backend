from django.contrib import admin
from django.urls import path, include 
from django.conf.urls import url
from patients import views

urlpatterns = [
    path('', include('patients.urls')),
    path('api/Fourteen', views.FourteenDayAvg, name='14dayavg')
]
