from simulation.tests.conftest import ComponentFactory, FeederFactory, ReceiverFactory


class TestComponent:
    def test_repr_method(self, db):
        receiver = ReceiverFactory()
        feeder = FeederFactory()
        component = ComponentFactory(name='A', receiver=receiver, feeder=feeder)

        assert component.__repr__() == (
            f'<Component(name=A, receiver_id={receiver.id}, received_at=None feeder_id={feeder.id})>'
        )
