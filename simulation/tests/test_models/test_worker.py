import pytest

from simulation.models import Component
from simulation.models.worker import Worker
from simulation.tests.conftest import WorkerFactory, ComponentFactory

pytestmark = pytest.mark.django_db


class TestWorker:
    @pytest.fixture
    def worker(self) -> Worker:
        return WorkerFactory()

    @pytest.fixture
    def component_a(self) -> Component:
        return ComponentFactory(name='A')

    def test_it_can_be_instantiated(self):
        worker = WorkerFactory(name='Billy Bob', slot_number=123)
        assert worker.name == 'Billy Bob'
        assert worker.slot_number == 123

    def test_it_pickups_up_a_component(self, worker, component_a):
        worker.conveyor_belt.enqueue(component_a)

        worker.work()
        assert worker.items == [component_a]

    def test_it_cannot_pickup_up_a_component_if_slot_used_by_another_worker(self, worker, component_a):
        # set slot to busy
        worker.conveyor_belt.put_item_in_slot(slot_number=0, item=component_a)

        worker.work()
        assert worker.items == []

    def test_it_does_not_pickup_component_if_already_owned(self, worker, component_a):
        conveyor_belt = worker.conveyor_belt

        for i in range(2):
            conveyor_belt.enqueue(component_a)
            conveyor_belt.dequeue()
            worker.work()

        assert worker.items == [component_a]
    #
    # def test_completes_pickup_operation_in_correct_time(
    #         self, worker_factory, basic_conveyor_belt: ConveyorBelt, worker_operation_times
    # ):
    #     basic_conveyor_belt.enqueue('A')
    #     worker = worker_factory(
    #         conveyor_belt=basic_conveyor_belt,
    #         operation_times=worker_operation_times
    #     )
    #
    #     for i in range(worker_operation_times.PICKING_UP):
    #         worker.work()
    #
    #     assert basic_conveyor_belt.is_slot_free(slot_number=0)
    #
    # def test_creates_product(self, worker_factory, basic_conveyor_belt):
    #     worker: Worker = worker_factory(conveyor_belt=basic_conveyor_belt)
    #
    #     feed_items = ['A', 'B', 'E', 'E', 'E', 'E']
    #     for feed_item in feed_items:
    #         basic_conveyor_belt.enqueue(feed_item)
    #         basic_conveyor_belt.dequeue()
    #         worker.work()
    #     assert worker.components == ['P']
    #
    # def test_drops_product(self, worker_factory, basic_conveyor_belt):
    #     worker: Worker = worker_factory(conveyor_belt=basic_conveyor_belt)
    #
    #     feed_items = ['A', 'B', 'E', 'E', 'E', 'E', 'E']
    #     for feed_item in feed_items:
    #         basic_conveyor_belt.enqueue(feed_item)
    #         basic_conveyor_belt.dequeue()
    #         worker.work()
    #     assert worker.components == []
    #
    # def test_completes_drop_product_operation_in_correct_time(
    #         self, worker_factory, basic_conveyor_belt, worker_operation_times
    # ):
    #     worker_operation_times.PICKING_UP = 1
    #     worker = worker_factory(
    #         conveyor_belt=basic_conveyor_belt,
    #         operation_times=worker_operation_times
    #     )
    #
    #     feed_items = ['A', 'B', 'E', 'E', 'E', 'E']
    #     for feed_item in feed_items:
    #         basic_conveyor_belt.enqueue(feed_item)
    #         basic_conveyor_belt.dequeue()
    #         worker.work()
    #     assert worker.components == ['P']
    #
    #     for i in range(worker_operation_times.DROPPING):
    #         worker.work()
    #
    #     assert worker.components == []
    #     assert basic_conveyor_belt.is_slot_free(slot_number=0)
    #
    # def test_cannot_drop_product_if_slot_is_used_by_another_worker(self, worker_factory, basic_conveyor_belt):
    #     worker: Worker = worker_factory(conveyor_belt=basic_conveyor_belt)
    #
    #     feed_items = ['A', 'B', 'E', 'E', 'E', 'E']
    #     for feed_item in feed_items:
    #         basic_conveyor_belt.enqueue(feed_item)
    #         basic_conveyor_belt.dequeue()
    #         worker.work()
    #
    #     basic_conveyor_belt.put_item_in_slot(slot_number=0, item='A')
    #     worker.work()
    #
    #     assert worker.components == ['P']