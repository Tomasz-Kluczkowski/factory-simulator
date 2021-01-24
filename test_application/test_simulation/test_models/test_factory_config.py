from datetime import datetime

from pytz import UTC

from simulation.models.factory_config import FactoryConfig
from test_application.conftest import FactoryConfigFactory


class TestFactoryConfig:
    def test_creation(self, db):
        factory_config: FactoryConfig = FactoryConfigFactory()

        assert factory_config.materials == ['A', 'B']
        assert factory_config.product_code == 'P'
        assert factory_config.empty_code == 'E'
        assert factory_config.number_of_simulation_steps == 10
        assert factory_config.number_of_conveyor_belt_slots == 3
        assert factory_config.number_of_worker_pairs == 3
        assert factory_config.simulation.name == 'Experiment 1'
        assert factory_config.simulation.description == 'Trying if stuff works'
        assert factory_config.simulation.start == datetime(2021, 1, 1, 12, tzinfo=UTC)
        assert factory_config.simulation.stop == datetime(2021, 1, 1, 13, tzinfo=UTC)
