from rest_framework import routers
from .views import UserViewSet, SetupViewSet, MedicationViewSet, GlucoseLevelViewSet, MedicationMasterViewSet

router = routers.DefaultRouter()
router.register('views/patients', UserViewSet, 'patients')
router.register('views/setup', SetupViewSet, 'setup')
router.register('views/medications', MedicationViewSet, 'medications')
router.register('views/glucoseLevels', GlucoseLevelViewSet, 'glucoseLevels')
router.register('views/MedicationMaster', MedicationMasterViewSet, 'MedicationMaster')

urlpatterns = router.urls