from datetime import datetime

from pytz import UTC

from simulation.models.simulation import Simulation
from test_application.conftest import SimulationFactory


class TestSimulation:
    def test_creation(self, db):
        simulation: Simulation = SimulationFactory()

        assert simulation.name == 'Experiment 1'
        assert simulation.description == 'Trying if stuff works'
        assert simulation.start == datetime(2021, 1, 1, 12, tzinfo=UTC)
        assert simulation.stop == datetime(2021, 1, 1, 13, tzinfo=UTC)
