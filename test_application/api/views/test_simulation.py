from rest_framework import status

import pytest
from django.urls import reverse

from simulation.models.simulation import Simulation
from test_application.conftest import SimulationFactory
from test_application.helpers import get_drf_iso_date

pytestmark = pytest.mark.django_db


class TestSimulationViewSet:
    def test_get_list_endpoint(self, client):
        simulation_1 = SimulationFactory()
        simulation_2 = SimulationFactory()

        response = client.get(path=reverse('api:simulations-list'))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2

        simulations = [simulation_1, simulation_2]
        for simulation, serialized_simulation in zip(simulations, response.data):
            assert simulation.id == serialized_simulation['id']
            assert simulation.name == serialized_simulation['name']
            assert simulation.description == serialized_simulation['description']
            assert get_drf_iso_date(simulation.start) == serialized_simulation['start']
            assert get_drf_iso_date(simulation.stop) == serialized_simulation['stop']

    def test_post_list_endpoint_with_relationships_data(self, client):
        salad_factory_config_data = {
            'materials': ['B', 'D'],
            'product_code': 'Salad',
            'empty_code': 'Empty',
            'number_of_simulation_steps': 20,
            'number_of_conveyor_belt_slots': 99,
            'number_of_worker_pairs': 4,
            'pickup_time': 3,
            'drop_time': 2,
            'build_time': 5,
        }

        burger_factory_config_data = {
            'materials': ['F'],
            'product_code': 'Burger',
            'empty_code': 'abyss',
            'number_of_simulation_steps': 11,
            'number_of_conveyor_belt_slots': 22,
            'number_of_worker_pairs': 33,
            'pickup_time': 44,
            'drop_time': 55,
            'build_time': 66,
        }

        salad_result_data = {
            'efficiency': 0.99
        }

        burger_result_data = {
            'efficiency': 0.34
        }

        simulation_data = {
            'name': 'test simulation',
            'description': 'some experiment to prove something',
            'start': '2021-01-27T12:00:00Z',
            'stop': '2021-01-27T13:00:00Z',
            'factory_configs': [salad_factory_config_data, burger_factory_config_data],
            'results': [salad_result_data, burger_result_data],
        }
        response = client.post(
            path=reverse('api:simulations-list'), data=simulation_data, content_type='application/json'
        )
        assert response.status_code == status.HTTP_201_CREATED

        simulation_id = response.data['id']
        simulation = Simulation.objects.get(id=simulation_id)

        assert simulation.name == simulation_data['name']
        assert simulation.description == simulation_data['description']
        assert get_drf_iso_date(simulation.start) == simulation_data['start']
        assert get_drf_iso_date(simulation.stop) == simulation_data['stop']

        factory_configs = simulation.factory_configs.all()
        assert len(factory_configs) == 2

        salad_factory_config = next(fc for fc in factory_configs if fc.product_code == 'Salad')
        for attribute, value in salad_factory_config_data.items():
            assert getattr(salad_factory_config, attribute) == value

        burger_factory_config = next(fc for fc in factory_configs if fc.product_code == 'Burger')
        for attribute, value in burger_factory_config_data.items():
            assert getattr(burger_factory_config, attribute) == value

        results = simulation.results.all()
        assert len(results) == 2

        salad_result = next(r for r in results if r.efficiency == 0.99)
        for attribute, value in salad_result_data.items():
            assert getattr(salad_result, attribute) == value

        burger_result = next(r for r in results if r.efficiency == 0.34)
        for attribute, value in burger_result_data.items():
            assert getattr(burger_result, attribute) == value

    def test_post_list_endpoint(self, client):
        simulation_data = {
            'name': 'test simulation',
            'description': 'some experiment to prove something',
            'start': '2021-01-27T12:00:00Z',
            'stop': '2021-01-27T13:00:00Z',
        }

        response = client.post(path=reverse('api:simulations-list'), data=simulation_data)
        assert response.status_code == status.HTTP_201_CREATED

        simulation_id = response.data['id']
        simulation = Simulation.objects.get(id=simulation_id)

        assert simulation.name == simulation_data['name']
        assert simulation.description == simulation_data['description']
        assert get_drf_iso_date(simulation.start) == simulation_data['start']
        assert get_drf_iso_date(simulation.stop) == simulation_data['stop']

    def test_get_detail_endpoint(self, client):
        simulation = SimulationFactory()

        response = client.get(reverse('api:simulations-detail', kwargs={'pk': simulation.pk}))
        assert response.status_code == status.HTTP_200_OK

        assert simulation.id == response.data['id']
        assert simulation.name == response.data['name']
        assert simulation.description == response.data['description']
        assert get_drf_iso_date(simulation.start) == response.data['start']
        assert get_drf_iso_date(simulation.stop) == response.data['stop']

    def test_put_detail_endpoint(self, client):
        simulation = SimulationFactory()
        simulation_data = {
            'name': 'test simulation',
            'description': 'some experiment to prove something',
            'start': '2021-01-27T12:11:00Z',
            'stop': '2021-01-27T13:12:00Z',
        }

        response = client.put(
            path=reverse('api:simulations-detail', kwargs={'pk': simulation.pk}),
            data=simulation_data,
            content_type='application/json'
        )
        assert response.status_code == status.HTTP_200_OK

        updated_simulation = Simulation.objects.get(id=simulation.id)
        assert updated_simulation.name == simulation_data['name']
        assert updated_simulation.description == simulation_data['description']
        assert get_drf_iso_date(updated_simulation.start) == simulation_data['start']
        assert get_drf_iso_date(updated_simulation.stop) == simulation_data['stop']

    def test_patch_detail_endpoint(self, client):
        simulation = SimulationFactory()
        simulation_data = {
            'name': 'new name',
        }

        response = client.patch(
            path=reverse('api:simulations-detail', kwargs={'pk': simulation.pk}),
            data=simulation_data,
            content_type='application/json'
        )
        assert response.status_code == status.HTTP_200_OK

        updated_simulation = Simulation.objects.get(id=simulation.id)
        assert updated_simulation.name == simulation_data['name']

    def test_delete_detail_endpoint(self, client):
        simulation = SimulationFactory()
        response = client.delete(path=reverse('api:simulations-detail', kwargs={'pk': simulation.pk}))
        assert response.status_code == status.HTTP_204_NO_CONTENT

        assert not Simulation.objects.filter(id=simulation.id).exists()
