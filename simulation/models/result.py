from django.db import models

from simulation.models.base_model import BaseModel
from simulation.models.simulation import Simulation


class Result(BaseModel):
    efficiency = models.DecimalField(max_digits=4, decimal_places=2)
    simulation = models.ForeignKey(Simulation, on_delete=models.CASCADE, related_name='results')
