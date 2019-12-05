"""
Here I want to have an object that will use config provided by the front end and instantiate
all the objects, save them in the DB and then have methods to run the optimisation and gather intermediate
/end state etc.
"""
from simulation.models import Feeder, Receiver, FactoryConfig, ConveyorBelt, FactoryFloor


class OptimisationRunner:
    def __init__(self):
        pass

    def prepare_simulation(self):
        """
        Uses config to create and persist all entities required to run simulation.
        """
        # TODO: make this from either API or some other form of config.
        feeder = Feeder.objects.create()
        receiver = Receiver.objects.create()
        factory_config = FactoryConfig.objects.create()
        conveyor_belt = ConveyorBelt.objects.create(factory_config=factory_config)
        factory_floor = FactoryFloor.objects.create(
            factory_config=factory_config,
            feeder=feeder,
            receiver=receiver,
            conveyor_belt=conveyor_belt
        )
        factory_floor.add_workers()

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
