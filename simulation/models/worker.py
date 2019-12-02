from typing import List, Union

from django.db import models

from simulation.models import BaseModel, Component, Product


class WorkerState:
    IDLE = 'idle'
    PICKING_UP = 'picking_up'
    DROPPING = 'dropping'
    BUILDING = 'building'

#
# class WorkerManager(models.Manager):
#     def get_worker_group_for_factory_floor(self, factory_floor_id):
#         return (
#             self.get_queryset()
#             .filter(factory_floor_id=factory_floor_id)
#             .select_related('operation_times', )
#         )


class WorkerOperationTimes(BaseModel):
    pick_up_time = models.PositiveSmallIntegerField(default=1)
    drop_time = models.PositiveSmallIntegerField(default=1)
    build_time = models.PositiveSmallIntegerField(default=4)


class Worker(BaseModel):
    name = models.CharField(max_length=30, blank=True, null=True, default='')
    slot_number = models.PositiveSmallIntegerField()
    operation_times = models.ForeignKey(WorkerOperationTimes, on_delete=models.CASCADE, related_name='workers')
    factory_floor = models.ForeignKey('FactoryFloor', on_delete=models.CASCADE, related_name='workers')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._items: List[Union[Component, Product]] = []
        self._current_state: str = WorkerState.IDLE
        self._remaining_time_of_operation: int = 0

    def work(self):
        """
        Guides work process of the worker. Below please find general assumptions.

        To simulate discrete worker's operation time we have to update _current_state at the beginning of each period,
        then update operation time if necessary and re-update state at the end of the period to take change in
        operation time into account.

        For example an operation which takes 1 period (picking up and dropping by default) starts and ends in the same
        tick of time.

        If operation takes more than one tick of time we carry out its task straight away but the state of affected
        slot of the conveyor belt will only update when the operation completes. This is to simplify things.

        I.e.: if picking up takes 2 ticks of time we update the _items list in the first tick of time but the
        affected conveyor belt slot remains busy until operation time drops to 0.
        """
        self._update_state()

        if self._is_operating():
            self._update_operation_time()

        self._update_state()

    def _update_state(self):
        """
        Updates state of the worker. We allow only one change of state per call to this method.
        """
        if self._current_state == WorkerState.IDLE:
            if self._can_pickup_component() and self._is_component_required():
                self._current_state = WorkerState.PICKING_UP
                self._on_picking_up_component()

            elif self._has_product() and self._can_drop_product():
                self._current_state = WorkerState.DROPPING
                self._on_dropping_product()

            elif self._is_ready_for_building():
                self._current_state = WorkerState.BUILDING
                self._on_building_product()

        elif self._current_state in [WorkerState.PICKING_UP, WorkerState.DROPPING]:
            if self._is_not_operating():
                self._current_state = WorkerState.IDLE
                self._on_finished_moving_goods()

        elif self._current_state == WorkerState.BUILDING:
            if self._is_not_operating():
                self._current_state = WorkerState.IDLE
                self._on_finished_building_product()

    @property
    def items(self):
        return self._items

    @property
    def item_names(self):
        return [item.name for item in self._items]

    @property
    def factory_config(self):
        return self.factory_floor.factory_config

    @property
    def conveyor_belt(self):
        return self.factory_floor.conveyor_belt

    def _can_pickup_component(self):
        return self.conveyor_belt.is_slot_free(self.slot_number)

    def _can_drop_product(self):
        return (
                self.conveyor_belt.is_slot_free(self.slot_number) and
                self.conveyor_belt.is_slot_empty(self.slot_number)
        )

    def _has_product(self):
        return self.factory_config.product_code in self.item_names

    def _is_operating(self):
        return self._remaining_time_of_operation > 0

    def _is_not_operating(self):
        return self._remaining_time_of_operation == 0

    def _is_ready_for_building(self):
        return len(self._items) == len(self.factory_config.required_component_names)

    def _is_component_required(self):
        item_on_belt = self.conveyor_belt.check_item_at_slot(self.slot_number)
        return (
                not self._has_product() and
                item_on_belt.name not in self.item_names and
                item_on_belt.name in self.factory_config.required_component_names
        )

    def _on_picking_up_component(self):
        self._remaining_time_of_operation = self.operation_times.pick_up_time

        item_at_slot = self.conveyor_belt.retrieve_item_from_slot(slot_number=self.slot_number)
        self._items.append(item_at_slot)

    def _on_dropping_product(self):
        self._remaining_time_of_operation = self.operation_times.drop_time
        self.conveyor_belt.put_item_in_slot(slot_number=self.slot_number, item=self._items.pop())

    def _on_building_product(self):
        self._remaining_time_of_operation = self.operation_times.build_time

    def _on_finished_moving_goods(self):
        self.conveyor_belt.confirm_operation_at_slot_finished(slot_number=self.slot_number)

    def _on_finished_building_product(self):
        self._items = []
        self._items.append(Product(name=self.factory_config.product_code))

    def _update_operation_time(self):
        self._remaining_time_of_operation -= 1
