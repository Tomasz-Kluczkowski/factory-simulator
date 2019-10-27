import pytest

from simulation.tests.conftest import FactoryFloorFactory, FeederFactory, ReceiverFactory, FactoryConfigFactory, \
    ConveyorBeltFactory

pytestmark = pytest.mark.django_db


class TestFactoryFloor:
    def test_it_can_be_instantiated(self):
        feeder = FeederFactory()
        receiver = ReceiverFactory()
        factory_config = FactoryConfigFactory()
        conveyor_belt = ConveyorBeltFactory(factory_config=factory_config)
        factory_floor = FactoryFloorFactory(
            factory_config=factory_config, feeder=feeder, receiver=receiver, conveyor_belt=conveyor_belt
        )

        assert factory_floor.factory_config == factory_config
        assert factory_floor.feeder == feeder
        assert factory_floor.receiver == receiver
        assert factory_floor.conveyor_belt == conveyor_belt
        assert factory_floor.time == 0



        # assert factory_floor.num_pairs == 3
        # assert len(factory_floor.workers) == 6
        # assert factory_floor.feeder == basic_feeder
        # assert factory_floor.receiver == basic_receiver
        # assert factory_floor.conveyor_belt.size == 3

    # def test_init_num_pairs(self, basic_feeder, basic_receiver, factory_floor_config):
    #     factory_floor_config.num_pairs = 1
    #     factory_floor = FactoryFloor(
    #         feeder=basic_feeder,
    #         receiver=basic_receiver,
    #         config=factory_floor_config
    #     )
    #
    #     assert len(factory_floor.workers) == 2
    #     assert factory_floor.feeder == basic_feeder
    #     assert factory_floor.receiver == basic_receiver
    #     assert factory_floor.conveyor_belt.size == 3
    #
    # def test_num_pairs_exceeding_num_slots(self, factory_floor_factory, factory_floor_config):
    #     factory_floor_config.num_pairs = 10
    #     with pytest.raises(FactoryConfigError) as exception:
    #         factory_floor_factory(config=factory_floor_config)
    #
    #     assert exception.value.args == (
    #         'Improperly configured FactoryFloor - num_pairs cannot exceed num_slots.',
    #     )
    #
    # def test_push_item_to_receiver(self, factory_floor_factory):
    #     factory_floor: FactoryFloor = factory_floor_factory()
    #     [factory_floor.conveyor_belt.dequeue() for _ in range(3)]
    #     [factory_floor.conveyor_belt.enqueue(i) for i in range(3)]
    #     factory_floor.push_item_to_receiver()
    #     assert factory_floor.receiver.received_items == [0]
    #     assert factory_floor.conveyor_belt.size == 2
    #
    # def test_add_new_item_to_belt(self, factory_floor_factory, feeder_factory, factory_floor_config):
    #     feeder = feeder_factory(feed_input=[1])
    #     factory_floor: FactoryFloor = factory_floor_factory(feeder=feeder)
    #     factory_floor.conveyor_belt.dequeue()
    #     factory_floor.add_new_item_to_belt()
    #     assert factory_floor.conveyor_belt.size == 3
    #     assert [factory_floor.conveyor_belt.dequeue() for i in range(3)] == [
    #         factory_floor_config.empty_code,
    #         factory_floor_config.empty_code,
    #         1
    #     ]
    #
    # def test_basic_run_belt(self, factory_floor_factory, feeder_factory, factory_floor_config):
    #     feeder = feeder_factory(feed_input=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    #     factory_floor: FactoryFloor = factory_floor_factory(feeder=feeder)
    #     factory_floor.run()
    #     assert factory_floor.receiver.received_items == [
    #         factory_floor_config.empty_code,
    #         factory_floor_config.empty_code,
    #         factory_floor_config.empty_code,
    #         1,
    #         2,
    #         3,
    #         4,
    #         5,
    #         6,
    #         7
    #     ]
    #
    #     assert factory_floor.time == 10
    #
    # def test_basic_run_belt_run_out_of_feed_items(self, factory_floor_factory, feeder_factory):
    #     feeder = feeder_factory(feed_input=[1])
    #     factory_floor: FactoryFloor = factory_floor_factory(feeder=feeder)
    #
    #     with pytest.raises(FactoryConfigError) as exception:
    #         factory_floor.run()
    #
    #     assert exception.value.args == (
    #         'Insufficient amount of items available in the feed_input of the Feeder. Please check your configuration.',
    #     )
    #
    # def test_run_factory_one_product_created_by_worker_on_slot_zero(
    #         self, factory_floor_factory, feeder_factory, factory_floor_config
    # ):
    #     factory_floor_config.num_steps = 11
    #     feeder = feeder_factory(
    #         feed_input=['A', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']
    #     )
    #     factory_floor: FactoryFloor = factory_floor_factory(
    #         config=factory_floor_config,
    #         feeder=feeder
    #     )
    #     factory_floor.run()
    #     assert factory_floor.receiver.received_items == ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'P', 'E']
    #
    # def test_run_factory_two_products_created_by_workers_on_slot_zero(
    #         self, factory_floor_factory, feeder_factory, factory_floor_config
    # ):
    #     factory_floor_config.num_steps = 13
    #     feeder = feeder_factory(
    #         feed_input=['A', 'B', 'A', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']
    #     )
    #     factory_floor: FactoryFloor = factory_floor_factory(
    #         config=factory_floor_config,
    #         feeder=feeder
    #     )
    #     factory_floor.run()
    #     assert factory_floor.receiver.received_items == [
    #         'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'P', 'E', 'P', 'E'
    #     ]
    #
    # def test_run_factory_three_products_created_by_workers_on_slot_zero_and_first_at_slot_one(
    #         self, factory_floor_factory, feeder_factory, factory_floor_config
    # ):
    #     factory_floor_config.num_steps = 15
    #     feeder = feeder_factory(
    #         feed_input=['A', 'B', 'A', 'B', 'A', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']
    #     )
    #     factory_floor: FactoryFloor = factory_floor_factory(
    #         config=factory_floor_config,
    #         feeder=feeder
    #     )
    #     factory_floor.run()
    #     assert factory_floor.receiver.received_items == [
    #         'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'P', 'E', 'P', 'E', 'P', 'E'
    #     ]
    #
    # def test_run_factory_worker_ignores_item_not_required(
    #         self, factory_floor_factory, feeder_factory, factory_floor_config
    # ):
    #     factory_floor_config.num_steps = 13
    #     factory_floor_config.num_pairs = 1
    #     feeder = feeder_factory(
    #         feed_input=['A', 'A', 'A', 'B', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']
    #     )
    #     factory_floor: FactoryFloor = factory_floor_factory(
    #         config=factory_floor_config,
    #         feeder=feeder
    #     )
    #     factory_floor.run()
    #     assert factory_floor.receiver.received_items == [
    #         'E', 'E', 'E', 'E', 'E', 'A', 'E', 'E', 'E', 'E', 'E', 'P', 'E'
    #     ]
