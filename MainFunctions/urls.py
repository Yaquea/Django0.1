from rest_framework import routers
from .api import PersonasViewsets

Routers= routers.DefaultRouter
Routers.register('api/personas', PersonasViewsets, 'personas' )

urlpatterns = Routers.urls