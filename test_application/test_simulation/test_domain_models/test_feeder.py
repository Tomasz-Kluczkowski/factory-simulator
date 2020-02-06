import random

from test_application.conftest import RandomizedFeederFactory, SequentialFeederFactory


class TestRandomizedFeeder:
    def test_it_can_be_instantiated(self):
        feeder = RandomizedFeederFactory()

        assert feeder

    def test_feed(self):
        random.seed(0)
        feeder = RandomizedFeederFactory()

        generated_items = []
        for i in range(4):
            generated_items.append(feeder.feed())

        expected_item_names_sequence = ['B', 'B', 'A', 'B']
        for item, name in zip(generated_items, expected_item_names_sequence):
            assert item.name == name


class TestSequentialFeeder:
    def test_it_can_be_instantiated(self):
        feeder = SequentialFeederFactory()

        assert feeder

    def test_feed(self):
        item_names = ('A', 'B', 'C')
        feeder = SequentialFeederFactory(item_names=item_names)

        for name in item_names:
            item = feeder.feed()
            assert item.name == name
