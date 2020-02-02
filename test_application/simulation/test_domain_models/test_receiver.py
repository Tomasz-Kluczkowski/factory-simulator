from datetime import datetime
from unittest.mock import patch

import pytest
from django.utils import timezone

from test_application.conftest import ReceiverFactory, ItemFactory


class TestReceiver:
    @pytest.fixture
    def receiver(self):
        return ReceiverFactory()

    @pytest.fixture
    def items(self, receiver):
        return [
            ItemFactory(received_at=datetime(2019, 1, 3, 12, 0, tzinfo=timezone.utc)),
            ItemFactory(received_at=datetime(2019, 1, 1, 12, 0, tzinfo=timezone.utc)),
            ItemFactory(received_at=datetime(2019, 1, 2, 12, 0, tzinfo=timezone.utc)),
        ]

    def test_it_can_be_instantiated(self):
        receiver = ReceiverFactory()

        assert receiver.received_items == []

    @patch('django.utils.timezone.now')
    def test_receive_sets_receiver_attribute_on_items(self, mock_now, receiver):
        received_at = datetime(2019, 1, 1, 12, 0, tzinfo=timezone.utc)
        mock_now.return_value = received_at
        item = ItemFactory()
        receiver.receive(item)

        assert receiver.received_items == [item]
        assert receiver.received_item_names == [item.name]
        assert item.received_at == received_at
