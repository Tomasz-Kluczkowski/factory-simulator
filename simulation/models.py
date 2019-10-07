import random
from typing import Union, Iterable, Sequence

from django.db import models

from simulation.exceptions.exceptions import FeederConfigError
from simulation.exceptions.messages import INVALID_FEED_INPUT


class Feeder(models.Model):
    """
    Use to provide feed for the conveyor belt. If no feed function specified will select random item from components
    list and return every time feed() is called on an instance.
    """
    def __init__(self, feed_input: Union[Iterable, Sequence] = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__feed_input = self.get_feed_input(feed_input) if feed_input else self.__default_feed_input()

    def __repr__(self):
        return f'<Feeder(id={self.id})>'

    def __default_feed_input(self):
        while True:
            yield random.choice(self.components.all().values_list('name', flat=True))

    @staticmethod
    def get_feed_input(feed_input: Union[Iterable, Sequence]):
        """
        Iterates over and returns items from feed_input.
        """
        if hasattr(feed_input, '__next__'):
            return feed_input
        try:
            feed_iterator = iter(feed_input)
            return feed_iterator
        except TypeError:
            raise FeederConfigError(INVALID_FEED_INPUT.format(object_type=feed_input.__class__.__name__))

    def feed(self):
        return next(self.__feed_input)


class Item(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    receiver = models.ForeignKey(
        'Receiver', on_delete=models.CASCADE, related_name='%(class)ss', null=True
    )
    received_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True


class Component(Item):
    feeder = models.ForeignKey(Feeder, null=True, on_delete=models.CASCADE, related_name='components')

    def __repr__(self):
        return (
            f'<Component(name={self.name}, receiver_id={self.receiver_id}, received_at={self.received_at} '
            f'feeder_id={self.feeder_id})>'
        )


class Product(Item):
    def __repr__(self):
        return f'<Product(name={self.name}, receiver_id={self.receiver_id}, received_at={self.received_at})>'


class Receiver(models.Model):
    """
    Use to receive items from the conveyor belt. Stores items in order of appearance and provides methods to obtain
    efficiency statistics for the plant operation.
    """

    def __repr__(self):
        return f'<Receiver(id={self.id})>'

    # @property
    # def received_items(self):
    #     return self.__received_items
    #
    # def receive(self, item):
    #     self.__received_items.append(item)
#
#
# class Product(Item):
