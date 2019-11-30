import pytest

from simulation.tests.conftest import ReceiverFactory, ProductFactory

pytestmark = pytest.mark.django_db


class TestProduct:
    def test_it_can_be_instantiated(self):
        receiver = ReceiverFactory()
        product = ProductFactory(id=1, name='B', receiver=receiver)

        assert product.id == 1
        assert product.name == 'B'
        assert product.receiver == receiver
        assert product.received_at is None
