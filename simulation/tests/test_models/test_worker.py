import pytest

from simulation.domain_models.conveyor_belt import ConveyorBelt
from simulation.domain_models.item import Item
from simulation.domain_models.worker import Worker
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
    def item_a(self) -> Item:
        return ItemFactory(name='A')

    def test_it_can_be_instantiated(self):
        worker = WorkerFactory(slot_number=123)
        assert worker.slot_number == 123

    def test_it_pickups_up_a_component(self, worker, item_a, conveyor_belt):
        conveyor_belt.enqueue(item_a)

        worker.work()
        assert worker.items == [item_a]

    def test_it_cannot_pickup_up_a_component_if_slot_used_by_another_worker(self, worker, item_a, conveyor_belt):
        # set slot to busy
        conveyor_belt.put_item_in_slot(slot_number=0, item=item_a)

        worker.work()
        assert worker.items == []

    def test_it_does_not_pickup_component_if_already_owned(self, worker, item_a, conveyor_belt):
        for i in range(2):
            conveyor_belt.enqueue(item_a)
            conveyor_belt.dequeue()
            worker.work()

        assert worker.items == [item_a]

    def test_it_completes_pickup_operation_in_correct_time(self, worker, item_a, conveyor_belt):
        conveyor_belt.enqueue(item_a)

        for i in range(worker.factory_config.pick_up_time):
            worker.work()

        assert conveyor_belt.is_slot_free(slot_number=0)

    def test_it_creates_product_in_correct_time(self, worker, conveyor_belt):
        feed_item_names = ['A', 'B', 'E', 'E', 'E', 'E']
        for feed_item_name in feed_item_names:
            item = ItemFactory(name=feed_item_name)
            conveyor_belt.enqueue(item)
            conveyor_belt.dequeue()
            worker.work()

        assert worker.item_names == ['P']

        [expected_product] = worker.items
        assert type(expected_product) is Item

    def test_it_drops_product_in_correct_time(self, worker, conveyor_belt):
        feed_item_names = ['A', 'B', 'E', 'E', 'E', 'E', 'E']
        for feed_item_name in feed_item_names:
            item = ItemFactory(name=feed_item_name)
            conveyor_belt.enqueue(item)
            conveyor_belt.dequeue()
            worker.work()

        assert worker.items == []

    def test_it_completes_drop_product_operation_in_correct_time(self, worker, conveyor_belt):
        feed_item_names = ['A', 'B', 'E', 'E', 'E', 'E']
        for feed_item_name in feed_item_names:
            item = ItemFactory(name=feed_item_name)
            conveyor_belt.enqueue(item)
            conveyor_belt.dequeue()
            worker.work()
        assert worker.item_names == ['P']

        for i in range(worker.factory_config.drop_time):
            worker.work()

        assert worker.items == []
        assert conveyor_belt.is_slot_free(slot_number=0)

    def test_it_cannot_drop_product_if_slot_is_used_by_another_worker(self, worker, conveyor_belt):
        feed_item_names = ['A', 'B', 'E', 'E', 'E', 'E']
        for feed_item_name in feed_item_names:
            item = ItemFactory(name=feed_item_name)
            conveyor_belt.enqueue(item)
            conveyor_belt.dequeue()
            worker.work()

        item = ItemFactory(name='A')
        conveyor_belt.put_item_in_slot(slot_number=0, item=item)
        worker.work()

        assert worker.item_names == ['P']
