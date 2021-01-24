import factory

from simulation.domain_models.conveyor_belt import ConveyorBelt
from simulation.domain_models.factory_floor import FactoryFloor
from simulation.domain_models.feeder import RandomizedFeeder, SequentialFeeder
from simulation.domain_models.item import Item
from simulation.domain_models.receiver import Receiver
from simulation.models.factory_config import FactoryConfig, get_default_materials
from simulation.domain_models.worker import Worker
from simulation.reporting.simulation_reporter import SimulationReporter


class ItemFactory(factory.Factory):
    class Meta:
        model = Item

    name = factory.Sequence(lambda n: f'component_{n}')


class RandomizedFeederFactory(factory.Factory):
    class Meta:
        model = RandomizedFeeder


class SequentialFeederFactory(factory.Factory):
    class Meta:
        model = SequentialFeeder


class ReceiverFactory(factory.Factory):
    class Meta:
        model = Receiver


class FactoryConfigFactory(factory.DjangoModelFactory):
    class Meta:
        model = FactoryConfig

    materials = get_default_materials()
    product_code = 'P'
    empty_code = 'E'
    number_of_simulation_steps = 10
    number_of_conveyor_belt_slots = 3
    number_of_worker_pairs = 3
    pickup_time = 1
    drop_time = 1
    build_time = 4


class ConveyorBeltFactory(factory.Factory):
    class Meta:
        model = ConveyorBelt

    factory_config = factory.SubFactory(FactoryConfigFactory)


class FactoryFloorFactory(factory.Factory):
    class Meta:
        model = FactoryFloor

    factory_config = factory.SubFactory(FactoryConfigFactory)
    feeder = factory.SubFactory(SequentialFeederFactory)
    receiver = factory.SubFactory(ReceiverFactory)
    conveyor_belt = factory.SubFactory(ConveyorBeltFactory, factory_config=factory.SelfAttribute('..factory_config'))


class WorkerFactory(factory.Factory):
    class Meta:
        model = Worker

    slot_number = factory.Sequence(lambda n: n)
    factory_floor = factory.SubFactory(FactoryFloorFactory)


class SimulationReporterFactory(factory.Factory):
    class Meta:
        model = SimulationReporter

    receiver = factory.SubFactory(ReceiverFactory)
    factory_config = factory.SubFactory(FactoryConfigFactory)
