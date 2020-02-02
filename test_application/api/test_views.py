from http import HTTPStatus

import pytest
from django.urls import reverse

from simulation.models.factory_config import FactoryConfig
from test_application.conftest import FactoryConfigFactory

pytestmark = pytest.mark.django_db


class TestFactoryConfigViewSet:
    def test_get_list_endpoint(self, client):
        factory_config_1 = FactoryConfigFactory()
        factory_config_2 = FactoryConfigFactory()

        response = client.get(reverse('api:factory-configs-list'))
        assert response.status_code == HTTPStatus.OK
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

    def test_post_list_endpoint(self, client):
        factory_config_data = {
            'required_item_names': ['B', 'D'],
            'product_code': 'Product',
            'empty_code': 'Empty',
            'number_of_simulation_steps': 20,
            'number_of_worker_pairs': 4,
            'pickup_time': 3,
            'drop_time': 2,
            'build_time': 5,
        }
        response = client.post(reverse('api:factory-configs-list'), factory_config_data)
        assert response.status_code == HTTPStatus.CREATED

        factory_config_id = response.data['id']
        factory_config = FactoryConfig.objects.get(id=factory_config_id)

        assert factory_config.required_item_names == factory_config_data['required_item_names']
        assert factory_config.product_code == factory_config_data['product_code']
        assert factory_config.empty_code == factory_config_data['empty_code']
        assert factory_config.number_of_simulation_steps == factory_config_data['number_of_simulation_steps']
        assert factory_config.number_of_worker_pairs == factory_config_data['number_of_worker_pairs']
        assert factory_config.pickup_time == factory_config_data['pickup_time']
        assert factory_config.drop_time == factory_config_data['drop_time']
        assert factory_config.build_time == factory_config_data['build_time']

    def test_get_detail_endpoint(self, client):
        factory_config = FactoryConfigFactory()

        response = client.get(reverse('api:factory-configs-detail', kwargs={'pk': factory_config.pk}))
        assert response.status_code == HTTPStatus.OK

        assert factory_config.id == response.data['id']
        assert factory_config.required_item_names == response.data['required_item_names']
        assert factory_config.product_code == response.data['product_code']
        assert factory_config.empty_code == response.data['empty_code']
        assert factory_config.number_of_simulation_steps == response.data['number_of_simulation_steps']
        assert factory_config.number_of_worker_pairs == response.data['number_of_worker_pairs']
        assert factory_config.pickup_time == response.data['pickup_time']
        assert factory_config.drop_time == response.data['drop_time']
        assert factory_config.build_time == response.data['build_time']
