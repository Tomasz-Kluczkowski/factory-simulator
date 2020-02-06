import random
from abc import ABC, abstractmethod
from typing import Iterator, Tuple

from simulation.domain_models.base_domain_model import BaseDomainModel
from simulation.domain_models.item import Item


class IFeeder(ABC):
    @abstractmethod
    def feed(self) -> Item:
        """
        Returns items one by one according to the pattern specified in the _feed_function.
        """
        pass

    @abstractmethod
    def _feed_function(self) -> Iterator[Item]:
        """
        Yields items in a specific pattern for the feed method.
        """
        pass


class Feeder(IFeeder, BaseDomainModel):
    def __init__(self, item_names: Tuple[str, ...] = ('A', 'B')):
        self._item_names = item_names
        self._pattern = self._feed_function()

    def feed(self) -> Item:
        """
        Returns items one by one according to the pattern specified in the _pattern.
        """
        item = next(self._pattern)
        return item

    def _feed_function(self) -> Iterator[Item]:
        """
        Yields items in a specific pattern for the feed method.
        """
        raise NotImplementedError


class RandomizedFeeder(Feeder):
    """
    Use to provide feed for the conveyor belt in random order by creating an item with a name from item_names.
    """
    def _feed_function(self) -> Iterator[Item]:
        """
        Yields items one by one in random order.
        """
        while True:
            item = Item(
                name=random.choice(self._item_names),
            )
            yield item


class SequentialFeeder(Feeder):
    """
    Use to provide a sequential feed based on order of _item_names for the conveyor belt.
    """
    def _feed_function(self) -> Iterator[Item]:
        return (Item(name=name) for name in self._item_names)
