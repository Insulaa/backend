from rest_framework import routers
from .views import PatientViewSet, SetupViewSet, MedicationViewSet, GlucoseLevelViewSet, MedicationMasterViewSet, FourteenDayAvg, GlucoseToday, CreateMed
from . import views

router = routers.DefaultRouter()
router.register('views/patients', PatientViewSet, 'patients')
router.register('views/setup', SetupViewSet, 'setup')
router.register('views/medications', MedicationViewSet, 'medications')
router.register('views/med', CreateMed, 'medications')
router.register('views/glucoseLevels', GlucoseLevelViewSet, 'glucoseLevels')
router.register('views/MedicationMaster', MedicationMasterViewSet, 'MedicationMaster')
router.register('FourteenDayAvg', FourteenDayAvg, '14Dayavg')
router.register('GlucoseToday', GlucoseToday, 'GlucoseToday')

urlpatterns = router.urls