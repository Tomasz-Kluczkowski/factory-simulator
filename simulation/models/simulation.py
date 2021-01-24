from django.db import models

from simulation.models.base_model import BaseModel


class Simulation(BaseModel):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255, blank=True, default='')
    start = models.DateTimeField()
    stop = models.DateTimeField(null=True)
