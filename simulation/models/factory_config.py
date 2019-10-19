from django.contrib.postgres.fields import ArrayField
from django.db import models

from simulation.models import BaseModel


def get_default_required_names():
    return ['A', 'B']


class FactoryConfig(BaseModel):
    required_component_names = ArrayField(
        models.CharField(max_length=30), default=get_default_required_names
    )
    product_code = models.CharField(max_length=30, default='P')
    empty_code = models.CharField(max_length=30, default='E')
    number_of_simulation_steps = models.PositiveIntegerField(default=10)
    number_of_conveyor_belt_slots = models.PositiveSmallIntegerField(default=3)
    number_of_worker_pairs = models.PositiveSmallIntegerField(default=3)

