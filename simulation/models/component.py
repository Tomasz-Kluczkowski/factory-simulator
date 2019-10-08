from django.db import models

from simulation.models import Item
from simulation.models.feeder import Feeder


class Component(Item):
    feeder = models.ForeignKey(Feeder, null=True, on_delete=models.CASCADE, related_name='components')
