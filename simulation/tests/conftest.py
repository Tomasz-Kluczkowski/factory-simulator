import factory

from simulation.models import Feeder, Component


class ComponentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Component

    name = factory.Sequence(lambda n: f'component_{n}')


class FeederFactory(factory.DjangoModelFactory):
    class Meta:
        model = Feeder
