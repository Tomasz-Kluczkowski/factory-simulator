from django.contrib import admin

from simulation.models.factory_config import FactoryConfig
from simulation.models.result import Result
from simulation.models.simulation import Simulation

admin.site.register(FactoryConfig)
admin.site.register(Result)
admin.site.register(Simulation)
