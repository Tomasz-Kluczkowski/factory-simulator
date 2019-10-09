import random

import pytest

from simulation.exceptions.exceptions import FeederConfigError
from simulation.tests.conftest import FeederFactory, ComponentFactory

pytestmark = pytest.mark.django_db


class TestFeeder:
    def test_it_can_be_instantiated(self):
        feeder = FeederFactory()
        component = ComponentFactory(feeder=feeder)

        assert list(feeder.components.all()) == [component]

    def test_feed_single_element_list(self):
        component = ComponentFactory()
        feeder = FeederFactory(feed_input=[component])
        assert feeder.feed() == component

    def test_feed_multiple_element_list(self):
        components = [ComponentFactory() for _ in range(3)]
        feeder = FeederFactory(feed_input=components)
        assert feeder.feed() == components[0]
        assert feeder.feed() == components[1]
        assert feeder.feed() == components[2]

    def test_feed_with_generator(self):
        components = (ComponentFactory(name=f'name_{i}') for i in range(3))
        feeder = FeederFactory(feed_input=components)
        for i in range(3):
            component = feeder.feed()
            assert component.name == f'name_{i}'
            assert component.feeder == feeder

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
        component_a = ComponentFactory(name='A', feeder=feeder)
        component_b = ComponentFactory(name='B', feeder=feeder)

        result = []
        for i in range(4):
            result.append(feeder.feed())

        assert result == [component_b, component_b, component_a, component_b]
