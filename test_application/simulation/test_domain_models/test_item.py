from datetime import datetime

from test_application.conftest import ItemFactory


class TestItem:
    def test_it_can_be_instantiated(self):
        received_at = datetime(2020, 1, 1, 12)
        item = ItemFactory(name='A', received_at=received_at)

        assert item.name == 'A'
        assert item.received_at == received_at
