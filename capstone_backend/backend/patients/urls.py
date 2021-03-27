from rest_framework import routers
from .views import LoginViewSet, RegisterUserViewSet, PatientViewSet, SetupViewSet, MedicationViewSet, GlucoseLevelViewSet, MedicationMasterViewSet, FourteenDayAvg, GlucoseToday
from . import views
from rest_framework.authtoken import views
from django.urls import path
from knox import views as knox_views

# router = routers.DefaultRouter()
# router.register('views/patients', PatientViewSet, 'patients')
# router.register('views/setup', SetupViewSet, 'setup')
# router.register('views/medications', MedicationViewSet, 'medications')
# router.register('views/glucoseLevels', GlucoseLevelViewSet, 'glucoseLevels')
# router.register('views/MedicationMaster', MedicationMasterViewSet, 'MedicationMaster')
# router.register('FourteenDayAvg', FourteenDayAvg, '14Dayavg')
# router.register('GlucoseToday', GlucoseToday, 'GlucoseToday')

# # Routes for Authentication
# router.register('auth/register', RegisterUserViewSet.as_view(), 'register')
# router.register('auth/login', LoginViewSet.as_view(), 'login')
# router.register('auth/logout', knox_views.LogoutView.as_view(), 'logout')

# urlpatterns = router.urls

urlpatterns = [
    path('views/patients', PatientViewSet, name='patients'),
    path('views/setup', SetupViewSet, name='setup'),
    path('views/medications', MedicationViewSet, name='medications'),
    path('views/glucoseLevels', GlucoseLevelViewSet, name='glucoseLevels'),
    path('views/medicationMaster', MedicationMasterViewSet, name='medicationMaster'),
    path('FourteenDayAvg', FourteenDayAvg, name='14Dayavg'),
    path('GlucoseToday', GlucoseToday, name='GlucoseToday'),
    path('auth/register', RegisterUserViewSet.as_view(), name='register'),
    path('auth/login', LoginViewSet.as_view(), name='login'),
    path('auth/logout', knox_views.LogoutView.as_view(), name='logout')
]