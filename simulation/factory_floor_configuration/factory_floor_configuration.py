from typing import List


class FactoryFloorConfig:
    def __init__(
            self,
            required_items: List[str] = None,
            product_code: str = None,
            num_steps: int = None,
            empty_code: str = None,
            conveyor_belt_slots: int = None,
            num_pairs: int = None
    ):
        self.required_items = required_items or ['A', 'B']
        self.product_code = product_code or 'P'
        self.num_steps = num_steps or 10
        self.empty_code = empty_code or 'E'
        self.conveyor_belt_slots = conveyor_belt_slots or 3
        self.num_pairs = num_pairs or 3
