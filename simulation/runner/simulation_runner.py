"""
Here I want to have an object that will use config provided by the front end and instantiate
all the objects, save them in the DB and then have methods to run the optimisation and gather intermediate
/end state etc.
"""
from simulation.models import Feeder, Receiver, FactoryConfig, ConveyorBelt, FactoryFloor


class OptimisationRunner:
    def __init__(
        self,
        feeder: Feeder,
        receiver: Receiver,
        factory_config: FactoryConfig,
        conveyor_belt: ConveyorBelt,
        factory_floor: FactoryFloor
    ):
        self._feeder = feeder
        self._receiver = receiver
        self._factory_config = factory_config
        self._conveyor_belt = conveyor_belt
        self._factory_floor = factory_floor

    def prepare_simulation(self):
        """
        Uses config to create and persist all entities required to run simulation.
        """
        self._factory_floor.add_workers()

    def run_simulation(self):
        """
        Runs the simulation.
        """
        pass

    def report_results(self):
        """
        Reports results of the simulation run.
        """
        pass
