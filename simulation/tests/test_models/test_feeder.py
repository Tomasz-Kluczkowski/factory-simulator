import random

import pytest
from simulation.models.feeder import sequential_feed_function
from simulation.tests.conftest import FeederFactory, ComponentFactory

pytestmark = pytest.mark.django_db


class TestFeedFunctions:
    def test_sequential_feed_function_with_empty_component_names(self):
        components_iterator = sequential_feed_function(component_names=(),)

        assert next(components_iterator, None) is None

    def test_sequential_feed_function(self):
        component_names = ('A', 'B', 'C')
        components_iterator = sequential_feed_function(component_names=component_names)

        for name in component_names:
            assert next(components_iterator).name == name


class TestFeeder:
    def test_it_can_be_instantiated(self):
        feeder = FeederFactory()
        component = ComponentFactory(feeder=feeder)

        assert list(feeder.components.all()) == [component]

    def test_with_sequential_feed_function(self):
        component_names = ('A', 'B', 'C')
        feeder = FeederFactory(
            component_names=component_names,
            feed_function=sequential_feed_function
        )

        for name in component_names:
            component = feeder.feed()
            assert component.name == name
            assert component.feeder_id == feeder.id

    def test_default_feed_function_and_default_component_names(self):
        random.seed(0)
        feeder = FeederFactory()

        generated_components = []
        for i in range(4):
            generated_components.append(feeder.feed())

        expected_component_names_sequence = ['B', 'B', 'A', 'B']
        for component, name in zip(generated_components, expected_component_names_sequence):
            assert component.name == name
            assert component.feeder_id == feeder.id
