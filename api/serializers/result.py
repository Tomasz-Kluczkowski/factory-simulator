from rest_framework import serializers

from simulation.models.result import Result


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['id', 'efficiency']
