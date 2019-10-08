import pytest

from simulation.tests.conftest import ReceiverFactory, ComponentFactory, ProductFactory

pytestmark = pytest.mark.django_db


class TestReceiver:
    def test_it_can_be_instantiated(self):
        receiver = ReceiverFactory()
        product = ProductFactory(receiver=receiver)
        component = ComponentFactory(receiver=receiver)

        assert receiver.id == 1
        assert list(receiver.products.all()) == [product]
        assert list(receiver.components.all()) == [component]
