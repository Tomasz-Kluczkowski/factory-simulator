from typing import List

from django.db.models import QuerySet
from django.utils import timezone

from simulation.models import BaseModel, Item


class Receiver(BaseModel):
    """
    Use to receive items from the conveyor belt. Stores items in order of appearance and provides methods to obtain
    efficiency statistics for the plant operation.
    """
    def receive(self, item: Item):
        item.receiver = self
        item.received_at = timezone.now()
        item.save()

    @property
    def received_items(self) -> QuerySet:
        return self.items.all().order_by('received_at')

    @property
    def received_item_names(self) -> List[str]:
        return list(self.received_items.values_list('name', flat=True))
