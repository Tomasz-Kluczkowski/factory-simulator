import random
from typing import Iterator, Callable, Tuple

from simulation.models import BaseModel
from simulation.models import Item


def sequential_feed_function(item_names: Tuple[str, ...]) -> Iterator['Item']:
    return (Item(name=name) for name in item_names)


class Feeder(BaseModel):
    """
    Use to provide feed for the conveyor belt.

    If feed_function is specified then it will be used to generate components.
    If no feed_function is provided we randomly generate a component with name from component_names and yield it.
    """
    def __init__(
            self,
            item_names: Tuple[str, ...] = ('A', 'B'),
            feed_function: Callable[[Tuple[str, ...]], Iterator[Item]] = None,
            *args,
            **kwargs
    ):
        super().__init__(*args, **kwargs)
        self._item_names = item_names
        self._feed_function = (
            feed_function(item_names=item_names) if feed_function else self._default_feed_function()
        )

    def _default_feed_function(self) -> Iterator[Item]:
        while True:
            item = Item(
                name=random.choice(self._item_names),
            )
            yield item

    def feed(self) -> Item:
        """
        Returns components according to __feed_function and sets the feeder attribute on each component if missing.
        """
        item = next(self._feed_function)
        item.feeder = self
        return item
