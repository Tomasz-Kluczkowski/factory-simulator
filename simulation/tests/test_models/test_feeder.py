import random

import pytest
from simulation.models.feeder import sequential_feed_function
from simulation.tests.conftest import FeederFactory, ItemFactory

pytestmark = pytest.mark.django_db


class TestFeedFunctions:
    def test_sequential_feed_function_with_empty_item_names(self):
        items_iterator = sequential_feed_function(item_names=(), )

        assert next(items_iterator, None) is None

    def test_sequential_feed_function(self):
        item_names = ('A', 'B', 'C')
        items_iterator = sequential_feed_function(item_names=item_names)

        for name in item_names:
            assert next(items_iterator).name == name


class TestFeeder:
    def test_it_can_be_instantiated(self):
        feeder = FeederFactory()
        item = ItemFactory(feeder=feeder)

        assert list(feeder.items.all()) == [item]

    def test_with_sequential_feed_function(self):
        item_names = ('A', 'B', 'C')
        feeder = FeederFactory(
            item_names=item_names,
            feed_function=sequential_feed_function
        )

        for name in item_names:
            item = feeder.feed()
            assert item.name == name
            assert item.feeder_id == feeder.id

    def test_default_feed_function_and_default_item_names(self):
        random.seed(0)
        feeder = FeederFactory()

        generated_items = []
        for i in range(4):
            generated_items.append(feeder.feed())

        expected_item_names_sequence = ['B', 'B', 'A', 'B']
        for item, name in zip(generated_items, expected_item_names_sequence):
            assert item.name == name
            assert item.feeder_id == feeder.id
