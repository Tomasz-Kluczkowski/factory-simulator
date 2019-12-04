"""
Here I want to have an object that will use config provided by the front end and instantiate
all the objects, save them in the DB and then have methods to run the optimisation and gather intermediate
/end state etc.
"""
from simulation.models import Feeder


class OptimisationRunner:
    def __init__(self):
        pass

    def prepare_simulation(self):
        """
        Uses config to create and persist all entities required to run simulation.
        """
        # TODO: make this from either API or some other form of config.
        feeder = Feeder.objects.create()
        receiver =


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
