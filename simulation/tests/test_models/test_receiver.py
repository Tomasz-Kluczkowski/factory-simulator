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

    def test_receive_sets_receiver_attribute_on_items(self):
        component = ComponentFactory()
        product = ProductFactory()
        receiver = ReceiverFactory()
        receiver.receive(component)
        receiver.receive(product)

        assert component.receiver == receiver
        assert product.receiver == receiver
