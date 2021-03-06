from rest_framework import viewsets

from api.serializers.simulation import SimulationSerializer
from simulation.models.simulation import Simulation
from simulation.tasks.tasks import run_simulation


class SimulationViewSet(viewsets.ModelViewSet):
    serializer_class = SimulationSerializer
    queryset = Simulation.objects.prefetch_related('factory_configs', 'results')

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        # TODO: create a dedicated endpoint for starting simulation and use it in the detail view in UI once the objects
        #  are successfully persisted - give a button. Initially just to run 1 factory config. Once we can do that -
        #  enable running each config in a simulation separately and have a run-all button as well.

        # TODO: move starting of the simulation into a dedicated endpoint away from here!
        run_simulation.delay(response.data['id'])

        return response
