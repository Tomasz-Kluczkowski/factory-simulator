import pytest
from django.urls import reverse

from simulation.tests.conftest import FactoryConfigFactory

pytestmark = pytest.mark.django_db


class TestFactoryConfigViewSet:
    def test_get_factory_configs_list_endpoint(self, client):
        factory_config_1 = FactoryConfigFactory()
        factory_config_2 = FactoryConfigFactory()

        response = client.get(reverse('api:factory-configs-list'))
        assert response.status_code == 200
        assert len(response.data) == 2

        factory_configs = [factory_config_1, factory_config_2]
        for config, serialized_config in zip(factory_configs, response.data):
            assert config.id == serialized_config['id']
            assert config.required_item_names == serialized_config['required_item_names']
            assert config.product_code == serialized_config['product_code']
            assert config.empty_code == serialized_config['empty_code']
            assert config.number_of_simulation_steps == serialized_config['number_of_simulation_steps']
            assert config.number_of_worker_pairs == serialized_config['number_of_worker_pairs']
            assert config.pickup_time == serialized_config['pickup_time']
            assert config.drop_time == serialized_config['drop_time']
            assert config.build_time == serialized_config['build_time']
