from django.db import models

from simulation.models import BaseModel


class WorkerState:
    IDLE = 'idle'
    PICKING_UP = 'picking_up'
    DROPPING = 'dropping'
    BUILDING = 'building'


class WorkerOperationTimes(BaseModel):
    pick_up_time = models.PositiveSmallIntegerField(null=False, default=1)
    drop_time = models.PositiveSmallIntegerField(null=False, default=1)
    build_time = models.PositiveSmallIntegerField(null=False, default=4)


# class Worker(BaseModel):
#     def __init__(self,
#                  config: FactoryFloorConfig,
#                  conveyor_belt: ConveyorBelt,
#                  slot_number: int,
#                  operation_times: Type[WorkerOperationTimes],
#                  name: str = '',
#                  ):
#         self.name = name
#         self._slot_number = slot_number
#         self._config = config
#         self._conveyor_belt = conveyor_belt
#         self._operation_times = operation_times
#         self._components = []
#         self._state = WorkerState.IDLE
#         self._remaining_time_of_operation = 0
#
#     def work(self):
#         """
#         Guides work process of the worker. Below please find general assumptions.
#
#         To simulate discrete worker's operation time we have to update state at the beginning of each period,
#         then update operation time if necessary and re-update state at the end of the period to take change in
#         operation time into account.
#
#         For example an operation which takes 1 period (picking up and dropping by default) starts and ends in the same
#         tick of time.
#
#         If operation takes more than one tick of time we carry out its task straight away but the state of affected
#         slot of the conveyor belt will only update when the operation completes. This is to simplify things.
#
#         I.e.: if picking up takes 2 ticks of time we update the components list in the first tick of time but the
#         affected conveyor belt slot remains busy until operation time drops to 0.
#         """
#         self._update_state()
#
#         if self._is_operating():
#             self._update_operation_time()
#
#         self._update_state()
#
#     def _update_state(self):
#         """
#         Updates state of the worker. We allow only one change of state per call to this method.
#         """
#         if self._state == WorkerState.IDLE:
#             if self._can_pickup_component() and self._is_component_required():
#                 self._state = WorkerState.PICKING_UP
#                 self._on_picking_up_component()
#
#             elif self._has_product() and self._can_drop_product():
#                 self._state = WorkerState.DROPPING
#                 self._on_dropping_product()
#
#             elif self._is_ready_for_building():
#                 self._state = WorkerState.BUILDING
#                 self._on_building_product()
#
#         elif self._state in [WorkerState.PICKING_UP, WorkerState.DROPPING]:
#             if self._is_not_operating():
#                 self._state = WorkerState.IDLE
#                 self._on_finished_moving_goods()
#
#         elif self._state == WorkerState.BUILDING:
#             if self._is_not_operating():
#                 self._state = WorkerState.IDLE
#                 self._on_finished_building_product()
#
#     @property
#     def components(self):
#         return self._components
#
#     def _can_pickup_component(self):
#         return self._conveyor_belt.is_slot_free(self._slot_number)
#
#     def _can_drop_product(self):
#         return (
#                 self._conveyor_belt.is_slot_free(self._slot_number) and
#                 self._conveyor_belt.is_slot_empty(self._slot_number)
#         )
#
#     def _has_product(self):
#         return self._config.product_code in self._components
#
#     def _is_operating(self):
#         return self._remaining_time_of_operation > 0
#
#     def _is_not_operating(self):
#         return self._remaining_time_of_operation == 0
#
#     def _is_ready_for_building(self):
#         return len(self._components) == len(self._config.required_items)
#
#     def _is_component_required(self):
#         item_on_belt = self._conveyor_belt.check_item_at_slot(self._slot_number)
#         return (
#                 not self._has_product() and
#                 item_on_belt not in self._components and
#                 item_on_belt in self._config.required_items
#         )
#
#     def _on_picking_up_component(self):
#         self._remaining_time_of_operation = self._operation_times.PICKING_UP
#
#         item_at_slot = self._conveyor_belt.retrieve_item_from_slot(slot_number=self._slot_number)
#         self._components.append(item_at_slot)
#
#     def _on_dropping_product(self):
#         self._remaining_time_of_operation = self._operation_times.DROPPING
#         self._conveyor_belt.put_item_in_slot(slot_number=self._slot_number, item=self._components.pop())
#
#     def _on_building_product(self):
#         self._remaining_time_of_operation = WorkerOperationTimes.BUILDING
#
#     def _on_finished_moving_goods(self):
#         self._conveyor_belt.confirm_operation_at_slot_finished(slot_number=self._slot_number)
#
#     def _on_finished_building_product(self):
#         self._components = []
#         self._components.append(self._config.product_code)
#
#     def _update_operation_time(self):
#         self._remaining_time_of_operation -= 1
