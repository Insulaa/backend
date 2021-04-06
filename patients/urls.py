from rest_framework import routers
from .views import GetUserIdWithTokenViewSet, LoginViewSet, RegisterUserViewSet, PatientViewSet, SetupViewSet, GetSingleMedication, GetMedicationCurrent, GetMedicationHistorical, EndMedication, MedicationViewSet, GlucoseLevelViewSet, MedicationMasterViewSet, FourteenDayAvg, GlucoseToday, BloodPressureViewSet
from . import views
from rest_framework.authtoken import views
from django.urls import path
from knox import views as knox_views

router = routers.DefaultRouter()
router.register('views/patients', PatientViewSet, 'patients')
router.register('views/setup', SetupViewSet, 'setup')
router.register('views/getSingleMedication', GetSingleMedication, 'getSingleMedication')
router.register('views/getMedicationsCurrent', GetMedicationCurrent, 'getMedicationsCurrent')
router.register('views/getMedicationsHistorical', GetMedicationHistorical, 'getMedicationsHistorical')
router.register('views/endMedication', EndMedication, 'endmedication') 
router.register('views/medications', MedicationViewSet, 'medications')
router.register('views/glucoseLevels', GlucoseLevelViewSet, 'glucoseLevels')
router.register('views/MedicationMaster', MedicationMasterViewSet, 'MedicationMaster')
router.register('views/FourteenDayAvg', FourteenDayAvg, '14Dayavg')
router.register('views/GlucoseToday', GlucoseToday, 'GlucoseToday')
router.register('views/BloodPressure', BloodPressureViewSet, 'BloodPressure')
router.register('auth/user', GetUserIdWithTokenViewSet, 'UserId')

# # Routes for Authentication
# router.register('auth/register', RegisterUserViewSet.as_view(), 'register')
# router.register('auth/login', LoginViewSet.as_view(), 'login')
# router.register('auth/logout', knox_views.LogoutView.as_view(), 'logout')

# urlpatterns = router.urls

urlpatterns = [
    # path('views/patients/', PatientViewSet.as_view({'get', 'post'}), name='patients'),
    # path('views/setup/', SetupViewSet.as_view({'get': 'list'}), name='setup'),
    # path('views/getSingleMedication/', GetSingleMedication.as_view({'get': 'list'}), name='getSingleMedication'),
    # path('views/getMedicationsCurrent/', GetMedicationCurrent.as_view({'get': 'list'}), name='getMedicationCurrent'),
    # path('views/getMedicationsHistorical/', GetMedicationHistorical.as_view({'get': 'list'}), name='getMedicationHistorical'),
    # path('views/endMedication/', EndMedication.as_view({'get': 'list'}), name='endmedication'),
    # path('views/medications/', MedicationViewSet.as_view({'get': 'list'}), name='medications'),
    # path('views/glucoseLevels/', GlucoseLevelViewSet.as_view({'get': 'list'}), name='glucoseLevels'),
    # path('views/medicationMaster/', MedicationMasterViewSet.as_view({'get': 'list'}), name='medicationMaster'),
    # path('FourteenDayAvg/', FourteenDayAvg.as_view({'get': 'list'}), name='14Dayavg'),
    # path('GlucoseToday/', GlucoseToday.as_view({'get': 'list'}), name='GlucoseToday'),
    path('auth/register/', RegisterUserViewSet.as_view(), name='register'),
    path('auth/login/', LoginViewSet.as_view(), name='login'),
    path('auth/logout/', knox_views.LogoutView.as_view(), name='logout')
]

urlpatterns += router.urls