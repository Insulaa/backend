from rest_framework import routers
from .views import PatientViewSet, SetupViewSet, GetSingleMedication, GetMedicationCurrent, GetMedicationHistorical, EndMedication, MedicationViewSet, GlucoseLevelViewSet, MedicationMasterViewSet, FourteenDayAvg, GlucoseToday
from . import views

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

urlpatterns = router.urls