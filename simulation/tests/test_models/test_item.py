from datetime import datetime

import pytest

from simulation.tests.conftest import ItemFactory

pytestmark = pytest.mark.django_db


class TestItem:
    def test_it_can_be_instantiated(self):
        received_at = datetime(2020, 1, 1, 12)
        item = ItemFactory(name='A', received_at=received_at)

        assert item.name == 'A'
        assert item.received_at == received_at
