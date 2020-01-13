from simulation.models import Receiver, FactoryConfig


class SimulationReporter:
    """
    Provides methods to obtain KPIs for the plant's operation.
    """
    def __init__(self, receiver: Receiver, factory_config: FactoryConfig):
        self._receiver = receiver
        self._factory_config = factory_config

    def get_production_efficiency(self) -> float:
        """
        Returns a simple calculation of production efficiency by dividing number of products received by total number
        of items.
        """
        items = self._receiver.received_item_names
        if not items:
            return 0

        number_of_products = items.count(self._factory_config.product_code)

        return number_of_products/len(items)
