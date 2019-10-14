import random
from typing import Iterator, Callable, Tuple

from simulation.models import BaseModel
from simulation.models import Component


def sequential_feed_function(component_names: Tuple[str, ...]) -> Iterator['Component']:
    return (Component(name=name) for name in component_names)


class Feeder(BaseModel):
    """
    Use to provide feed for the conveyor belt.

    If feed_function is specified then it will be used to generate components.
    If no feed_function is provided we randomly generate a component with name from component_names and yield it.
    """
    def __init__(
            self,
            component_names: Tuple[str, ...] = ('A', 'B'),
            feed_function: Callable[[Tuple[str, ...]], Iterator[Component]] = None,
            *args,
            **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.__component_names = component_names
        self.__feed_function = (
            feed_function(component_names=component_names) if feed_function else self.__default_feed_function()
        )

    def __default_feed_function(self) -> Iterator[Component]:
        while True:
            component = Component(
                name=random.choice(self.__component_names),
            )
            yield component

    def feed(self) -> Component:
        """
        Returns components according to __feed_function and sets the feeder attribute on each component if missing.
        """
        component = next(self.__feed_function)
        if component.feeder_id is None:
            component.feeder = self
        return component
