from django.contrib.postgres.fields import ArrayField
from django.db import models

from simulation.models.base_model import BaseModel


def get_default_materials():
    return ['A', 'B']


class FactoryConfig(BaseModel):
    materials = ArrayField(
        models.CharField(max_length=30)
    )
    product_code = models.CharField(max_length=30)
    empty_code = models.CharField(max_length=30)
    number_of_simulation_steps = models.PositiveIntegerField()
    number_of_conveyor_belt_slots = models.PositiveSmallIntegerField()
    number_of_worker_pairs = models.PositiveSmallIntegerField()
    pickup_time = models.PositiveSmallIntegerField()
    drop_time = models.PositiveSmallIntegerField()
    build_time = models.PositiveSmallIntegerField()
