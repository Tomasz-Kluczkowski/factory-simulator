from simulation.models.factory_config import FactoryConfig
from test_application.conftest import FactoryConfigFactory


class TestWorkerOperationTimes:
    def test_default_values_are_set(self, db):
        default_factory_config: FactoryConfig = FactoryConfigFactory()

        assert default_factory_config.materials == ['A', 'B']
        assert default_factory_config.product_code == 'P'
        assert default_factory_config.empty_code == 'E'
        assert default_factory_config.number_of_simulation_steps == 10
        assert default_factory_config.number_of_conveyor_belt_slots == 3
        assert default_factory_config.number_of_worker_pairs == 3
