from rest_framework import serializers

from simulation.models import FactoryConfig


class FactoryConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactoryConfig
        fields = [
            'required_item_names',
            'product_code',
            'empty_code',
            'number_of_simulation_steps',
            'number_of_conveyor_belt_slots',
            'number_of_worker_pairs',
        ]
