import pytest

from simulation.models import Item, ConveyorBelt
from simulation.models.worker import Worker
from simulation.tests.conftest import WorkerFactory, ItemFactory

pytestmark = pytest.mark.django_db


class TestWorker:
    @pytest.fixture
    def worker(self) -> Worker:
        return WorkerFactory(slot_number=0)

    @pytest.fixture
    def conveyor_belt(self, worker) -> ConveyorBelt:
        return worker.conveyor_belt

    @pytest.fixture
    def component_a(self) -> Component:
        return ComponentFactory(name='A')

    def test_it_can_be_instantiated(self):
        worker = WorkerFactory(name='Billy Bob', slot_number=123)
        assert worker.name == 'Billy Bob'
        assert worker.slot_number == 123

    def test_it_pickups_up_a_component(self, worker, component_a, conveyor_belt):
        conveyor_belt.enqueue(component_a)

        worker.work()
        assert worker.items == [component_a]

    def test_it_cannot_pickup_up_a_component_if_slot_used_by_another_worker(self, worker, component_a, conveyor_belt):
        # set slot to busy
        conveyor_belt.put_item_in_slot(slot_number=0, item=component_a)

        worker.work()
        assert worker.items == []

    def test_it_does_not_pickup_component_if_already_owned(self, worker, component_a, conveyor_belt):
        for i in range(2):
            conveyor_belt.enqueue(component_a)
            conveyor_belt.dequeue()
            worker.work()

        assert worker.items == [component_a]

    def test_it_completes_pickup_operation_in_correct_time(self, worker, component_a, conveyor_belt):
        conveyor_belt.enqueue(component_a)

        for i in range(worker.operation_times.pick_up_time):
            worker.work()

        assert conveyor_belt.is_slot_free(slot_number=0)

    def test_it_creates_product_in_correct_time(self, worker, conveyor_belt):
        feed_item_names = ['A', 'B', 'E', 'E', 'E', 'E']
        for feed_item_name in feed_item_names:
            component = ComponentFactory(name=feed_item_name)
            conveyor_belt.enqueue(component)
            conveyor_belt.dequeue()
            worker.work()

        assert worker.item_names == ['P']

        [expected_product] = worker.items
        assert type(expected_product) is Product

    def test_it_drops_product_in_correct_time(self, worker, conveyor_belt):
        feed_item_names = ['A', 'B', 'E', 'E', 'E', 'E', 'E']
        for feed_item_name in feed_item_names:
            component = ComponentFactory(name=feed_item_name)
            conveyor_belt.enqueue(component)
            conveyor_belt.dequeue()
            worker.work()

        assert worker.items == []

    def test_it_completes_drop_product_operation_in_correct_time(self, worker, conveyor_belt):
        feed_item_names = ['A', 'B', 'E', 'E', 'E', 'E']
        for feed_item_name in feed_item_names:
            component = ComponentFactory(name=feed_item_name)
            conveyor_belt.enqueue(component)
            conveyor_belt.dequeue()
            worker.work()
        assert worker.item_names == ['P']

        for i in range(worker.operation_times.drop_time):
            worker.work()

        assert worker.items == []
        assert conveyor_belt.is_slot_free(slot_number=0)

    def test_it_cannot_drop_product_if_slot_is_used_by_another_worker(self, worker, conveyor_belt):
        feed_item_names = ['A', 'B', 'E', 'E', 'E', 'E']
        for feed_item_name in feed_item_names:
            component = ComponentFactory(name=feed_item_name)
            conveyor_belt.enqueue(component)
            conveyor_belt.dequeue()
            worker.work()

        component = ComponentFactory(name='A')
        conveyor_belt.put_item_in_slot(slot_number=0, item=component)
        worker.work()

        assert worker.item_names == ['P']
