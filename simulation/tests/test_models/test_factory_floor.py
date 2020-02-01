from unittest.mock import Mock

import pytest

from simulation.exceptions.exceptions import FactoryConfigError
from simulation.models import FactoryFloor
from simulation.domain_models.feeder import sequential_feed_function
from simulation.tests.conftest import FactoryFloorFactory, FeederFactory, ReceiverFactory, FactoryConfigFactory, \
    ConveyorBeltFactory, ItemFactory

pytestmark = pytest.mark.django_db


class TestFactoryFloor:
    @pytest.fixture
    def feeder(self):
        return FeederFactory()

    @pytest.fixture
    def receiver(self):
        return ReceiverFactory()

    @pytest.fixture
    def factory_config(self):
        return FactoryConfigFactory()

    @pytest.fixture
    def conveyor_belt(self, factory_config):
        return ConveyorBeltFactory(factory_config=factory_config)

    @pytest.fixture
    def factory_floor(self, factory_config, feeder, receiver, conveyor_belt) -> FactoryFloor:
        return FactoryFloorFactory(
            factory_config=factory_config, feeder=feeder, receiver=receiver, conveyor_belt=conveyor_belt
        )

    def test_it_can_be_instantiated(self, feeder, receiver, factory_config, conveyor_belt, factory_floor):
        assert factory_floor.factory_config == factory_config
        assert factory_floor.feeder == feeder
        assert factory_floor.receiver == receiver
        assert factory_floor.conveyor_belt == conveyor_belt
        assert factory_floor.time == 0

    def test_add_workers_default_operation_times_used(self, factory_floor):
        factory_floor.add_workers()

        workers = factory_floor.workers
        assert len(workers) == 6

        assert sorted([worker.slot_number for worker in workers]) == [0, 0, 1, 1, 2, 2]

        for worker in workers:
            assert worker.factory_config == factory_floor.factory_config
            assert worker.conveyor_belt == factory_floor.conveyor_belt
            assert worker.factory_floor == factory_floor

    def test_add_workers_custom_operation_times_used(self, factory_floor):
        factory_floor.add_workers()

        workers = factory_floor.workers
        assert len(workers) == 6

        assert sorted([worker.slot_number for worker in workers]) == [0, 0, 1, 1, 2, 2]

        for worker in workers:
            assert worker.factory_config == factory_floor.factory_config
            assert worker.conveyor_belt == factory_floor.conveyor_belt
            assert worker.factory_floor == factory_floor

    def test_raises_exception_if_number_of_worker_pairs_exceeds_number_of_conveyor_belt_slots(self):
        factory_config = FactoryConfigFactory(number_of_worker_pairs=3, number_of_conveyor_belt_slots=1)
        with pytest.raises(FactoryConfigError) as exception:
            FactoryFloorFactory(factory_config=factory_config)

        assert exception.value.args == (
                'Improperly configured FactoryFloor - check factory_config. number_of_worker_pairs cannot exceed '
                'number_of_conveyor_belt_slots.',
        )

    def test_push_item_to_receiver(self, factory_floor):
        factory_floor.push_item_to_receiver()
        assert factory_floor.conveyor_belt.size == 2
        assert factory_floor.receiver.received_item_names == [factory_floor.factory_config.empty_code]

    def test_add_new_item_to_belt(self, factory_floor):
        item = ItemFactory(name='A')
        mock_feed = Mock()
        mock_feed.return_value = item
        factory_floor.feeder.feed = mock_feed

        factory_floor.conveyor_belt.dequeue()
        factory_floor.add_new_item_to_belt()

        assert factory_floor.conveyor_belt.size == 3
        assert [factory_floor.conveyor_belt.dequeue().name for i in range(3)] == [
            factory_floor.factory_config.empty_code,
            factory_floor.factory_config.empty_code,
            item.name
        ]

    def test_basic_run_belt(self, factory_floor):
        feeder = FeederFactory(
            item_names=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
            feed_function=sequential_feed_function
        )
        factory_floor: FactoryFloor = FactoryFloorFactory(feeder=feeder)
        factory_floor.run()
        assert factory_floor.receiver.received_item_names == [
            factory_floor.factory_config.empty_code,
            factory_floor.factory_config.empty_code,
            factory_floor.factory_config.empty_code,
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7'
        ]

        assert factory_floor.time == 10

    def test_basic_run_belt_run_out_of_feed_items(self):
        feeder = FeederFactory(item_names=['1'], feed_function=sequential_feed_function)
        factory_floor: FactoryFloor = FactoryFloorFactory(feeder=feeder)

        with pytest.raises(FactoryConfigError) as exception:
            factory_floor.run()

        assert exception.value.args == (
            'Insufficient amount of items available in the feed_input of the Feeder. Please check your configuration.',
        )

    def test_run_factory_one_product_created_by_worker_on_slot_zero(self):
        feeder = FeederFactory(
            item_names=['A', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            feed_function=sequential_feed_function
        )

        factory_floor: FactoryFloor = FactoryFloorFactory(
            feeder=feeder
        )
        factory_floor.factory_config.number_of_simulation_steps = 11
        factory_floor.add_workers()
        factory_floor.run()

        assert factory_floor.receiver.received_item_names == ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'P', 'E']

    def test_run_factory_two_products_created_by_workers_on_slot_zero(self):
        feeder = FeederFactory(
            item_names=['A', 'B', 'A', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            feed_function=sequential_feed_function
        )
        factory_floor: FactoryFloor = FactoryFloorFactory(
            feeder=feeder
        )
        factory_floor.factory_config.number_of_simulation_steps = 13
        factory_floor.add_workers()
        factory_floor.run()

        assert factory_floor.receiver.received_item_names == [
            'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'P', 'E', 'P', 'E'
        ]

    def test_run_factory_three_products_created_by_workers_on_slot_zero_and_first_at_slot_one(self):
        feeder = FeederFactory(
            item_names=['A', 'B', 'A', 'B', 'A', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            feed_function=sequential_feed_function
        )
        factory_floor: FactoryFloor = FactoryFloorFactory(
            feeder=feeder
        )
        factory_floor.factory_config.number_of_simulation_steps = 15
        factory_floor.add_workers()
        factory_floor.run()

        assert factory_floor.receiver.received_item_names == [
            'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'P', 'E', 'P', 'E', 'P', 'E'
        ]

    def test_run_factory_worker_ignores_item_not_required(self):
        feeder = FeederFactory(
            item_names=['A', 'A', 'A', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            feed_function=sequential_feed_function
        )
        factory_floor: FactoryFloor = FactoryFloorFactory(
            feeder=feeder
        )
        factory_floor.factory_config.number_of_simulation_steps = 13
        factory_floor.factory_config.number_of_worker_pairs = 1
        factory_floor.add_workers()
        factory_floor.run()

        assert factory_floor.receiver.received_item_names == [
            'E', 'E', 'E', 'E', 'E', 'A', 'E', 'E', 'E', 'E', 'E', 'P', 'E'
        ]
