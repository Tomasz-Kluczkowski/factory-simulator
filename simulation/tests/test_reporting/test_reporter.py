import pytest
from django.utils import timezone

from simulation.tests.conftest import ItemFactory, FactoryConfigFactory, ReceiverFactory, SimulationReporterFactory

pytestmark = pytest.mark.django_db


class TestSimulationReporter:
    @pytest.fixture
    def factory_config(self):
        return FactoryConfigFactory()

    @pytest.fixture
    def receiver(self):
        return ReceiverFactory()

    @pytest.fixture
    def product_item(self, factory_config):
        return ItemFactory(name=factory_config.product_code, received_at=timezone.now())

    def test_it_calculates_production_efficiency(self, factory_config, receiver, product_item):
        items = [
            ItemFactory(
                name=factory_config.empty_code, received_at=timezone.now()
            ) for __ in range(3)
        ]
        items.append(product_item)
        for item in items:
            receiver.receive(item)

        simulation_reporter = SimulationReporterFactory(receiver=receiver, factory_config=factory_config)

        assert simulation_reporter.get_production_efficiency() == 1/4

    def test_it_works_with_no_products(self, factory_config, receiver):
        [
            ItemFactory(
                name=factory_config.empty_code, received_at=timezone.now()
            ) for __ in range(3)
        ]

        simulation_reporter = SimulationReporterFactory(receiver=receiver, factory_config=factory_config)

        assert simulation_reporter.get_production_efficiency() == 0

    def test_it_works_with_no_items(self, factory_config, receiver):
        simulation_reporter = SimulationReporterFactory(receiver=receiver, factory_config=factory_config)

        assert simulation_reporter.get_production_efficiency() == 0
