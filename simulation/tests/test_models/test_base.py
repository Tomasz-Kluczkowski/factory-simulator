from simulation.models.base import BaseModel


class TestBaseModel:
    def test_str_method(self):
        class BaseChild(BaseModel):
            pass
        base_child = BaseChild(id='test_id')
        assert str(base_child) == '<BaseChild(id=test_id)>'
