from django.contrib import admin

from simulation.models import Component, Product, Feeder, Receiver

admin.site.register(Component)
admin.site.register(Product)
admin.site.register(Feeder)
admin.site.register(Receiver)
