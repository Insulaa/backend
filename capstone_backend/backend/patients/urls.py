from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register('views/patients', UserViewSet, 'patients')

urlpatterns = router.urls