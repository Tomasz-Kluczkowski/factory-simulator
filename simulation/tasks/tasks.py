from factory_simulator.celery import celery_app
from simulation.domain_models.conveyor_belt import ConveyorBelt
from simulation.domain_models.factory_floor import FactoryFloor
from simulation.domain_models.feeder import RandomizedFeeder
from simulation.domain_models.receiver import Receiver
from simulation.models.simulation import Simulation


@celery_app.task
def run_simulation(simulation_id: str):
    # TODO: confirm how many queries this makes if there are multiple factory configs!
    simulation = Simulation.objects.select_related().prefetch_related('factory_configs', 'results').get(id=simulation_id)
    factory_configs = simulation.factory_configs.all()

    # TODO: this should be run per factory config once all deemed ok.
    factory_config = factory_configs[0]

    # TODO: feeder type should be configurable from the front end
    feeder = RandomizedFeeder(item_names=(*factory_config.materials, factory_config.empty_code))
    receiver = Receiver()
    factory_floor = FactoryFloor(
        feeder=feeder,
        receiver=receiver,
        conveyor_belt=ConveyorBelt(factory_config=factory_config),
        factory_config=factory_config
    )
    factory_floor.add_workers()

    factory_floor.run()

    print(receiver.received_item_names)
