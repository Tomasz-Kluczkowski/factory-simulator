from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views.factory_config import FactoryConfigViewSet
from api.views.simulation import SimulationViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'factory-configs', FactoryConfigViewSet, basename='factory-configs')
router.register(r'simulations', SimulationViewSet, basename='simulations')

urlpatterns = [
    path('', include(router.urls)),
]
