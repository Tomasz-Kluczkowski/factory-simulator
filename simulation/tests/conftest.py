import factory

from simulation.models import Feeder, Component, Receiver, Product, WorkerOperationTimes, ConveyorBelt
from simulation.models.factory_config import FactoryConfig
from simulation.models.worker import Worker


class ProductFactory(factory.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: f'product_{n}')


class ComponentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Component

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


class WorkerFactory(factory.DjangoModelFactory):
    class Meta:
        model = Worker

    operation_times = factory.SubFactory(WorkerOperationTimesFactory)
    slot_number = factory.Sequence(lambda n: n)
    factory_config = factory.SubFactory(FactoryConfigFactory)
    conveyor_belt = factory.SubFactory(ConveyorBeltFactory)
