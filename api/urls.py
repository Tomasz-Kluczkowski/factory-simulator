from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import FactoryConfigViewSet

router = DefaultRouter()
router.register(r'factory-configs', FactoryConfigViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
