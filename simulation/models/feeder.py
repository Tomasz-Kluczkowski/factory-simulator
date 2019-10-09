import random
from typing import Union, Iterable, Sequence

from simulation.exceptions.exceptions import FeederConfigError
from simulation.exceptions.messages import INVALID_FEED_INPUT
from simulation.models import BaseModel
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from simulation.models import Component


class Feeder(BaseModel):
    """
    Use to provide feed for the conveyor belt. If no feed function specified will select random item from components
    list and return every time feed() is called on an instance.
    """
    def __init__(self, feed_input: Union[Iterable['Component'], Sequence['Component']] = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__feed_input = self.__get_feed_input(feed_input) if feed_input else self.__default_feed_input()

    def __default_feed_input(self):
        while True:
            yield random.choice(self.components.all())

    @staticmethod
    def __get_feed_input(feed_input: Union[Iterable['Component'], Sequence['Component']]):
        if hasattr(feed_input, '__next__'):
            return feed_input
        try:
            feed_iterator = iter(feed_input)
            return feed_iterator
        except TypeError:
            raise FeederConfigError(INVALID_FEED_INPUT.format(object_type=feed_input.__class__.__name__))

    def feed(self) -> 'Component':
        """
        Return components in a sequence.
        """
        return next(self.__feed_input)
