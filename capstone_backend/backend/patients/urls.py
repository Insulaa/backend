from rest_framework import routers
from .views import UserViewSet, SetupViewSet, MedicationViewSet

router = routers.DefaultRouter()
router.register('views/patients', UserViewSet, 'patients')
router.register('views/setup', SetupViewSet, 'setup')
router.register('views/medications', MedicationViewSet, 'medications')

urlpatterns = router.urls