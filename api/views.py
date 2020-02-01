from rest_framework import viewsets

from api.serializers.factory_config import FactoryConfigSerializer
from simulation.models.factory_config import FactoryConfig


class FactoryConfigViewSet(viewsets.ModelViewSet):
    serializer_class = FactoryConfigSerializer
    queryset = FactoryConfig.objects.all()
