import pytest

from simulation.domain_models.conveyor_belt import ConveyorBelt
from simulation.domain_models.item import Item
from simulation.tests.conftest import ConveyorBeltFactory

pytestmark = pytest.mark.django_db


class TestConveyorBelt:
    def test_it_can_be_instantiated(self):
        conveyor_belt: ConveyorBelt = ConveyorBeltFactory()

        assert conveyor_belt.slot_states == {
            0: 'free',
            1: 'free',
            2: 'free',
        }
        assert conveyor_belt.size == 3
        for item in conveyor_belt.items:
            assert item.name == conveyor_belt.factory_config.empty_code

    def test_check_item_at_slot_with_item_present(self):
        conveyor_belt = ConveyorBeltFactory()
        conveyor_belt.enqueue(1)

        assert conveyor_belt.check_item_at_slot(0) == 1

    def test_check_item_at_slot_with_item_not_present(self):

        conveyor_belt = ConveyorBeltFactory()

        assert conveyor_belt.check_item_at_slot(0).name == conveyor_belt.factory_config.empty_code

    def test_put_item_in_slot_adds_item_and_sets_slot_to_busy(self):
        conveyor_belt: ConveyorBelt = ConveyorBeltFactory()
        item = Item(name='A')
        conveyor_belt.put_item_in_slot(slot_number=0, item=item)

        assert conveyor_belt.check_item_at_slot(slot_number=0) == item
        assert conveyor_belt.is_slot_busy(slot_number=0)

    def test_confirm_operation_finished_changes_slot_state_to_free(self):
        conveyor_belt: ConveyorBelt = ConveyorBeltFactory()
        item = Item(name='A')
        conveyor_belt.put_item_in_slot(slot_number=0, item=item)

        assert conveyor_belt.is_slot_busy(slot_number=0)
        conveyor_belt.confirm_operation_at_slot_finished(slot_number=0)
        assert not conveyor_belt.is_slot_busy(slot_number=0)

    def test_is_slot_busy_returns_true(self):
        conveyor_belt: ConveyorBelt = ConveyorBeltFactory()
        conveyor_belt.put_item_in_slot(slot_number=0, item=Item(name='A'))

        assert conveyor_belt.is_slot_busy(0)

    def test_is_slot_busy_returns_false(self):
        conveyor_belt: ConveyorBelt = ConveyorBeltFactory()

        assert not conveyor_belt.is_slot_busy(0)

    def test_is_slot_empty_returns_true(self):
        conveyor_belt: ConveyorBelt = ConveyorBeltFactory()

        assert conveyor_belt.is_slot_empty(0)

    def test_is_slot_empty_returns_false(self):
        conveyor_belt: ConveyorBelt = ConveyorBeltFactory()
        conveyor_belt.enqueue(Item(name='A'))

        assert not conveyor_belt.is_slot_empty(0)

    def test_is_slot_free_returns_true(self):
        conveyor_belt: ConveyorBelt = ConveyorBeltFactory()
        assert conveyor_belt.is_slot_free(slot_number=0)

    def test_is_slot_free_returns_false(self):
        conveyor_belt: ConveyorBelt = ConveyorBeltFactory()
        conveyor_belt.put_item_in_slot(slot_number=0, item=Item(name='A'))

        assert not conveyor_belt.is_slot_free(slot_number=0)

    def test_retrieve_item_from_slot(self):
        conveyor_belt: ConveyorBelt = ConveyorBeltFactory()
        item = Item(name='A')
        conveyor_belt.enqueue(item)

        assert conveyor_belt.retrieve_item_from_slot(slot_number=0) == item
        assert conveyor_belt.is_slot_busy(slot_number=0)
        assert conveyor_belt.check_item_at_slot(slot_number=0).name == conveyor_belt.factory_config.empty_code
