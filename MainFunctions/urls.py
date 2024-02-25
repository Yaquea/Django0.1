from rest_framework import routers
from .api import PersonasViewsets

router = routers.DefaultRouter()
router.register('api/personas', PersonasViewsets, 'personas')

urlpatterns = router.urls