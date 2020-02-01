from dataclasses import dataclass

from simulation.domain_models.base import BaseDomainModel


class TestBaseDomainModel:
    def test_str_method(self):
        @dataclass
        class BaseChild(BaseDomainModel):
            name: str
        base_child = BaseChild(name='Tom')
        assert str(base_child) == '<BaseChild(name=Tom)>'
