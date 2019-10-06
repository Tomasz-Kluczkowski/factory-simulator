import random
from unittest import mock

import pytest
from devtools import debug

from simulation.exceptions.exceptions import FeederConfigError
from simulation.tests.conftest import FeederFactory, ComponentFactory

pytestmark = pytest.mark.django_db


class TestFeeder:
    def test_feed_single_element_list(self):
        feeder = FeederFactory(feed_input=[1])
        assert feeder.feed() == 1

    def test_feed_multiple_element_list(self):
        feeder = FeederFactory(feed_input=[1, 2, 3])
        assert feeder.feed() == 1
        assert feeder.feed() == 2
        assert feeder.feed() == 3

    def test_feed_with_generator(self):
        feeder = FeederFactory(feed_input=(item for item in [1, 2, 3]))
        assert feeder.feed() == 1
        assert feeder.feed() == 2
        assert feeder.feed() == 3

    def test_feed_not_iterable(self):

        with pytest.raises(FeederConfigError) as exception:
            FeederFactory(feed_input=True)

        assert exception.value.args == (
            (
                'Unable to iterate over supplied feed_input of type: bool. Please make sure feed_input is an Iterable '
                'or a Sequence.'
            ),
        )

    def test_default_feed(self):
        random.seed(0)
        feeder = FeederFactory()
        ComponentFactory(name='A', feeder=feeder)
        ComponentFactory(name='B', feeder=feeder)

        result = []
        for i in range(4):
            result.append(feeder.feed())

        assert result == ['B', 'B', 'A', 'B']
