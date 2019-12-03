from typing import Any, Union

from django.db import models

from simulation.helpers.data_structures import Queue
from simulation.models import BaseModel, FactoryConfig, Item


class ConveyorBeltState:
    FREE = 'free'
    BUSY = 'busy'


class ConveyorBelt(BaseModel, Queue):
    factory_config = models.ForeignKey(FactoryConfig, on_delete=models.CASCADE, related_name='conveyor_belts')

    def __init__(self, *args, **kwargs):
        super(). __init__(*args, **kwargs)
        self._slot_states = {}
        self._set_slot_states_to_free()
        self._set_slots_to_empty()

    # TODO: override enqueue, deque and include typing for input/output

    @property
    def slot_states(self):
        return self._slot_states

    def check_item_at_slot(self, slot_number: int) -> Item:
        """
        Returns item at a conveyor belt slot. The item remains in the slot. This is a peek operation.

        Parameters
        ----------
        slot_number
            Slot of the conveyor belt at which we need to check for item.
        Returns
        -------
            Item at the slot_number.
        """
        return self._items[slot_number]

    def put_item_in_slot(self, slot_number: int, item: Item):
        """
        Inserts item at a given slot_number.

        Parameters
        ----------
        slot_number
            Slot of the conveyor belt at which we need to insert the item.
        item
            Item which we want to insert.
        """
        self._set_slot_state(slot_number=slot_number, state=ConveyorBeltState.BUSY)
        self._items[slot_number] = item

    def confirm_operation_at_slot_finished(self, slot_number: int):
        """
        Confirms that the operation that was being carried out on slot slot_number has finished.
        This sets the state of that slot back to free.

        Parameters
        ----------
        slot_number
            Slot of the conveyor belt at which we need to insert the item.
        """
        self._set_slot_state(slot_number=slot_number, state=ConveyorBeltState.FREE)

    def is_slot_busy(self, slot_number: int) -> bool:
        """
        Returns a boolean: True is slot is busy, false if free.

        Parameters
        ----------
        slot_number
            Slot of the conveyor belt at which we need to check if busy.
        """
        return self._get_slot_state(slot_number) == ConveyorBeltState.BUSY

    def is_slot_empty(self, slot_number: int) -> bool:
        """
        Returns a boolean: True is slot is empty, false if not.

        Parameters
        ----------
        slot_number
            Slot of the conveyor belt at which we need to check if empty.
        """

        return self._items[slot_number].name == self.factory_config.empty_code

    def is_slot_free(self, slot_number: int) -> bool:
        """
        Returns a boolean: True is slot is free, false if busy.

        Parameters
        ----------
        slot_number
            Slot of the conveyor belt at which we need to check if free.
        """
        return self._get_slot_state(slot_number) == ConveyorBeltState.FREE

    def retrieve_item_from_slot(self, slot_number: int) -> Any:
        """
        Returns an item present in the slot: slot_number, sets the slot to busy and puts an empty Component in
        its place.

        Parameters
        ----------
        slot_number
            Slot of the conveyor belt from which we want to retrieve the item.

        Returns
        -------
        item
            Item in the slot with slot_number.
        """
        self._set_slot_state(slot_number=slot_number, state=ConveyorBeltState.BUSY)
        item = self.check_item_at_slot(slot_number=slot_number)
        self.put_item_in_slot(slot_number=slot_number, item=Item(name=self.factory_config.empty_code))

        return item

    def _set_slot_states_to_free(self):
        for slot_number in range(self.factory_config.number_of_conveyor_belt_slots):
            self._slot_states[slot_number] = ConveyorBeltState.FREE

    def _set_slots_to_empty(self):
        for slot_number in range(self.factory_config.number_of_conveyor_belt_slots):
            self.enqueue(Item(name=self.factory_config.empty_code))

    def _set_slot_state(self, slot_number: int, state: str):
        self._slot_states[slot_number] = state

    def _get_slot_state(self, slot_number: int) -> Union[str, None]:
        return self._slot_states.get(slot_number)
