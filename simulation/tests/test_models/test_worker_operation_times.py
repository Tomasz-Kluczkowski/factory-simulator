from simulation.tests.conftest import WorkerOperationTimesFactory


class TestWorkerOperationTimes:
    def test_default_values_are_set(self, db):
        default_worker_operation_times = WorkerOperationTimesFactory()

        assert default_worker_operation_times.pick_up_time == 1
        assert default_worker_operation_times.drop_time == 1
        assert default_worker_operation_times.build_time == 4
