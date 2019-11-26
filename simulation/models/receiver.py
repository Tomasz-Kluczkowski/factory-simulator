from typing import Union

from django.utils import timezone

from simulation.models import BaseModel, Component, Product


class Receiver(BaseModel):
    """
    Use to receive items from the conveyor belt. Stores items in order of appearance and provides methods to obtain
    efficiency statistics for the plant operation.
    """
    def receive(self, item: Union[Component, Product]):
        item.receiver = self
        item.received_at = timezone.now()
        item.save()

    @property
    def received_items(self):
        # TODO: improve the query - use prefetch? Switch to one type of object? Just Item?
        components = list(self.components.all())
        products = list(self.products.all())
        return sorted(components + products, key=lambda item: item.received_at)

    @property
    def received_item_names(self):
        return [obj.name for obj in self.received_items]
