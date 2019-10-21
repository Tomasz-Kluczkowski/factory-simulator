import pytest

from simulation.tests.conftest import ComponentFactory, FeederFactory, ReceiverFactory

pytestmark = pytest.mark.django_db


class TestComponent:
    def test_it_can_be_instantiated(self):
        receiver = ReceiverFactory()
        feeder = FeederFactory()
        component = ComponentFactory(name='A', receiver=receiver, feeder=feeder)

        assert component.id == 1
        assert component.name == 'A'
        assert component.receiver == receiver
        assert component.feeder == feeder
        assert component.received_at is None
