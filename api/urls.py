from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import FactoryConfigViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'factory-configs', FactoryConfigViewSet, basename='factory-configs')

urlpatterns = [
    path('', include(router.urls)),
]
