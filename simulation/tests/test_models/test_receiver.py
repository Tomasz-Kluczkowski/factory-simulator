from datetime import datetime
from unittest.mock import patch
from django.utils import timezone

import pytest

from simulation.tests.conftest import ReceiverFactory, ItemFactory

pytestmark = pytest.mark.django_db


class TestReceiver:
    @pytest.fixture
    def receiver(self):
        return ReceiverFactory()

    @pytest.fixture
    def items(self, receiver):
        return [
            ItemFactory(receiver=receiver, received_at=datetime(2019, 1, 3, 12, 0, tzinfo=timezone.utc)),
            ItemFactory(receiver=receiver, received_at=datetime(2019, 1, 1, 12, 0, tzinfo=timezone.utc)),
            ItemFactory(receiver=receiver, received_at=datetime(2019, 1, 2, 12, 0, tzinfo=timezone.utc)),
        ]

    def test_it_can_be_instantiated(self):
        receiver = ReceiverFactory(id=1)

        assert receiver.id == 1

    @patch('django.utils.timezone.now')
    def test_receive_sets_receiver_attribute_on_items(self, mock_now, receiver):
        received_at = datetime(2019, 1, 1, 12, 0, tzinfo=timezone.utc)
        mock_now.return_value = received_at
        item = ItemFactory()
        receiver.receive(item)

        assert item.receiver == receiver
        assert item.received_at == received_at

    def test_received_items_are_sorted_by_time(self, receiver, items):
        assert list(receiver.received_items) == sorted(items, key=lambda i: i.received_at)

    def test_received_item_names_are_sorted_by_time(self, receiver, items):
        sorted_item_names = [i.name for i in sorted(items, key=lambda i: i.received_at)]
        assert receiver.received_item_names == sorted_item_names
