from rest_framework import serializers

from api.serializers.factory_config import FactoryConfigSerializer
from api.serializers.result import ResultSerializer
from simulation.models.factory_config import FactoryConfig
from simulation.models.result import Result
from simulation.models.simulation import Simulation


class SimulationSerializer(serializers.ModelSerializer):
    factory_configs = FactoryConfigSerializer(many=True, required=False)
    results = ResultSerializer(many=True, required=False)

    class Meta:
        model = Simulation
        fields = ['id', 'name', 'description', 'start', 'stop', 'factory_configs', 'results']

    def create(self, validated_data):
        factory_configs_data = validated_data.pop('factory_configs', None)
        results_data = validated_data.pop('results', None)

        simulation = Simulation.objects.create(**validated_data)

        if factory_configs_data:
            for factory_config_data in factory_configs_data:
                FactoryConfig.objects.create(simulation=simulation, **factory_config_data)

        if results_data:
            for result_data in results_data:
                Result.objects.create(simulation=simulation, **result_data)

        return simulation
