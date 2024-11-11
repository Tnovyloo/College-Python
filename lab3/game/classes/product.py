from typing import Dict
from .item import Item
from .resource import Resource
from collections import defaultdict

class Product(Item):
    def __init__(self, name: str, price: float, required_items: Dict[Item, int] = None):
        super().__init__(name, price)
        self.required_items = required_items if required_items else {}

    def get_info(self):
        info = f"Product: {self.name}\nPrice: {self.price}\nResources needed:"
        if self.required_items:
            for item, quantity in self.required_items.items():
                info += f"\n\t{item.name}: {quantity}"
        else:
            info += "\n\tNone"
        return info

    def get_total_resources(self) -> Dict[Resource, int]:
        """Wyznacza rekurencyjnie słownik wszystkich zasobów potrzebnych do stworzenia przedmiotu."""
        total_resources = defaultdict(int)

        def collect_resources(item: Item, quantity: int):
            if isinstance(item, Resource):
                total_resources[item] += quantity
            elif isinstance(item, Product):
                for sub_item, sub_quantity in item.required_items.items():
                    collect_resources(sub_item, sub_quantity * quantity)

        for item, quantity in self.required_items.items():
            collect_resources(item, quantity)

        return dict(total_resources)
