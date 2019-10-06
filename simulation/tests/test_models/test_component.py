from simulation.tests.conftest import ComponentFactory


class TestComponent:
    def test_repr_method(self, db):
        component = ComponentFactory(name='A')

        assert component.__repr__() == '<Component(name=A)>'
