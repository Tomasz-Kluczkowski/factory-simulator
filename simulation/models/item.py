from django.db import models

from simulation.models import BaseModel


class Item(BaseModel):
    name = models.CharField(max_length=30)
    receiver = models.ForeignKey(
        'Receiver', on_delete=models.CASCADE, related_name='%(class)ss', null=True
    )
    received_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True
