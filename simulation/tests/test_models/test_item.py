import pytest

from simulation.tests.conftest import ItemFactory, FeederFactory, ReceiverFactory

pytestmark = pytest.mark.django_db


class TestItem:
    def test_it_can_be_instantiated(self):
        receiver = ReceiverFactory()
        feeder = FeederFactory()
        item = ItemFactory(name='A', receiver=receiver, feeder=feeder)

        assert item.id == 1
        assert item.name == 'A'
        assert item.receiver == receiver
        assert item.feeder == feeder
        assert item.received_at is None
