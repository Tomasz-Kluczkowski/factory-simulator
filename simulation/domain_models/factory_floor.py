from simulation.domain_models.base_domain_model import BaseDomainModel
from simulation.domain_models.conveyor_belt import ConveyorBelt
from simulation.domain_models.feeder import Feeder
from simulation.domain_models.receiver import Receiver
from simulation.exceptions.exceptions import FactoryConfigError
from simulation.exceptions.messages import WRONG_FACTORY_CONFIG, INSUFFICIENT_FEED_INPUT
from simulation.domain_models.worker import Worker
from simulation.models.factory_config import FactoryConfig


class FactoryFloor(BaseDomainModel):
    """
    This is the controller of the entire operation. It will navigate the production line.
    By default the number of pairs matches the number of slots on the belt.
    """
    def __init__(
            self, feeder: Feeder, receiver: Receiver, conveyor_belt: ConveyorBelt, factory_config: FactoryConfig
    ):
        self._workers = []
        self.feeder = feeder
        self.receiver = receiver
        self.conveyor_belt = conveyor_belt
        self.factory_config = factory_config
        if self.factory_config.number_of_worker_pairs > self.factory_config.number_of_conveyor_belt_slots:
            raise FactoryConfigError(WRONG_FACTORY_CONFIG)
        self.time = 0

    def add_workers(self):
        """
        Creates a pair of workers per self.factory_config.number_of_worker_pairs and saves in the database.
        Each worker pair is assigned to a slot_number on the conveyor belt.
        """
        for slot_number in range(self.factory_config.number_of_worker_pairs):
            for pair_number in range(2):
                worker = Worker(
                    slot_number=slot_number,
                    factory_floor=self
                )
                self._workers.append(worker)

    def push_item_to_receiver(self):
        """
        Moves last item on the belt to the receiver.
        """
        item_to_receive = self.conveyor_belt.dequeue()
        self.receiver.receive(item_to_receive)

    def add_new_item_to_belt(self):
        """
        Adds new item to the conveyor belt.
        """
        new_belt_item = self.feeder.feed()
        self.conveyor_belt.enqueue(new_belt_item)

    def run(self):
        """
        Main event loop.
        """
        for step in range(self.factory_config.number_of_simulation_steps):
            self.push_item_to_receiver()

            try:
                self.add_new_item_to_belt()
            except StopIteration:
                raise FactoryConfigError(INSUFFICIENT_FEED_INPUT)

            # make each pair work
            for worker in self._workers:
                worker.work()
            self.time += 1

    @property
    def workers(self):
        return self._workers
