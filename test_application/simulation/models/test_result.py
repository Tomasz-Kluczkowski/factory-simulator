from datetime import datetime

from pytz import UTC

from simulation.models.result import Result
from test_application.conftest import ResultFactory


class TestResult:
    def test_creation(self, db):
        result: Result = ResultFactory()

        assert result.efficiency == 33.29
        assert result.simulation.name == 'Experiment 1'
        assert result.simulation.description == 'Trying if stuff works'
        assert result.simulation.start == datetime(2021, 1, 1, 12, tzinfo=UTC)
        assert result.simulation.stop == datetime(2021, 1, 1, 13, tzinfo=UTC)
