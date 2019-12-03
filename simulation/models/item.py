from django.db import models

from simulation.models import BaseModel


class Item(BaseModel):
    name = models.CharField(max_length=30)
    feeder = models.ForeignKey('Feeder', null=True, on_delete=models.CASCADE, related_name='items')
    receiver = models.ForeignKey('Receiver', null=True, on_delete=models.CASCADE, related_name='items')
    received_at = models.DateTimeField(blank=True, null=True)
