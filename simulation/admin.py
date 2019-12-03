from django.contrib import admin

from simulation.models import Feeder, Receiver, Item

admin.site.register(Item)
admin.site.register(Feeder)
admin.site.register(Receiver)
