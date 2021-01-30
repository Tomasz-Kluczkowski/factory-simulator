from rest_framework import viewsets

from api.serializers.simulation import SimulationSerializer
from simulation.models.simulation import Simulation


class SimulationViewSet(viewsets.ModelViewSet):
    serializer_class = SimulationSerializer
    queryset = Simulation.objects.prefetch_related('factory_configs', 'results')
