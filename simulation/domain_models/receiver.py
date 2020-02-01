from typing import List

from django.utils import timezone

from simulation.domain_models.base_domain_model import BaseDomainModel
from simulation.domain_models.item import Item


class Receiver(BaseDomainModel):
    """
    Use to receive items from the conveyor belt. Stores items in order of appearance.
    """
    def __init__(self):
        self._received_items: List[Item] = []

    def receive(self, item: Item):
        item.received_at = timezone.now()
        self._received_items.append(item)

    @property
    def received_items(self) -> List[Item]:
        return self._received_items

    @property
    def received_item_names(self) -> List[str]:
        return [item.name for item in self._received_items]
