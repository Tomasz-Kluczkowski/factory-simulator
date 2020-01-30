from dataclasses import dataclass
from datetime import datetime

from django.db import models

from simulation.domain_models.base import BaseDomainModel


@dataclass
class Item(BaseDomainModel):
    name: str = models.CharField(max_length=30)
    received_at: datetime = None
