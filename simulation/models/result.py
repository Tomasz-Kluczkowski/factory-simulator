from django.db import models

from simulation.models.base_model import BaseModel
from simulation.models.simulation import Simulation


class Result(BaseModel):
    efficiency = models.FloatField()
    simulation = models.ForeignKey(Simulation, on_delete=models.CASCADE, related_name='results')
