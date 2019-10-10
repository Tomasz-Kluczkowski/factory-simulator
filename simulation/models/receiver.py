from typing import Union

from simulation.models import BaseModel, Component, Product


class Receiver(BaseModel):
    """
    Use to receive items from the conveyor belt. Stores items in order of appearance and provides methods to obtain
    efficiency statistics for the plant operation.
    """
    pass

    # TODO: we have to convert feeder to operate on components and here
    #  we want to proceed with components/products
    # @property
    # def received_items(self):
    #     return self.__received_items
    #

    def receive(self, item: Union[Component, Product]):
        item.receiver = self
