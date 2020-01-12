import factory

from simulation.models import Feeder, Receiver, WorkerOperationTimes, ConveyorBelt, FactoryFloor, Item
from simulation.models.factory_config import FactoryConfig
from simulation.models.worker import Worker
from simulation.reporting.simulation_reporter import SimulationReporter


class ItemFactory(factory.DjangoModelFactory):
    class Meta:
        model = Item

    name = factory.Sequence(lambda n: f'component_{n}')


class FeederFactory(factory.DjangoModelFactory):
    class Meta:
        model = Feeder


class ReceiverFactory(factory.DjangoModelFactory):
    class Meta:
        model = Receiver


class WorkerOperationTimesFactory(factory.DjangoModelFactory):
    class Meta:
        model = WorkerOperationTimes


class FactoryConfigFactory(factory.DjangoModelFactory):
    class Meta:
        model = FactoryConfig


class ConveyorBeltFactory(factory.DjangoModelFactory):
    class Meta:
        model = ConveyorBelt

    factory_config = factory.SubFactory(FactoryConfigFactory)


class FactoryFloorFactory(factory.DjangoModelFactory):
    class Meta:
        model = FactoryFloor

    factory_config = factory.SubFactory(FactoryConfigFactory)
    feeder = factory.SubFactory(FeederFactory)
    receiver = factory.SubFactory(ReceiverFactory)
    conveyor_belt = factory.SubFactory(ConveyorBeltFactory, factory_config=factory.SelfAttribute('..factory_config'))


class WorkerFactory(factory.DjangoModelFactory):
    class Meta:
        model = Worker

    operation_times = factory.SubFactory(WorkerOperationTimesFactory)
    slot_number = factory.Sequence(lambda n: n)
    factory_floor = factory.SubFactory(FactoryFloorFactory)


class SimulationReporterFactory(factory.Factory):
    class Meta:
        model = SimulationReporter

    receiver = factory.SubFactory(ReceiverFactory)
    factory_config = factory.SubFactory(FactoryConfigFactory)
