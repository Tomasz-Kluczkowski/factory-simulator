import random
from typing import Iterator, Callable, Tuple

from simulation.domain_models.base import BaseDomainModel
from simulation.domain_models.item import Item


def sequential_feed_function(item_names: Tuple[str, ...]) -> Iterator['Item']:
    return (Item(name=name) for name in item_names)


class Feeder(BaseDomainModel):
    """
    Use to provide feed for the conveyor belt.

    If feed_function is specified then it will be used to generate items.
    If no feed_function is provided we randomly generate an item with name from item_names and yield it.
    """
    def __init__(
            self,
            item_names: Tuple[str, ...] = ('A', 'B'),
            feed_function: Callable[[Tuple[str, ...]], Iterator[Item]] = None,
    ):
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
        Returns items according to __feed_function and sets the feeder attribute on each item if missing.
        """
        item = next(self._feed_function)
        return item
