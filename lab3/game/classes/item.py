from abc import ABC
from abc import abstractmethod

class Item(ABC):
    def __init__(self, name: str, price: float):
        if not name:
            raise ValueError("Nazwa nie moze byc none")
        self._name = name

        if price < 0:
            raise ValueError("Cena nie moze byc mniejsza od 0.")
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Cena nie moze byc mniejsza od 0.")
        self._price = value

    @abstractmethod
    def get_info(self):
        pass

    def __lt__(self, other):
        if isinstance(other, Item):
            return self.name < other.name
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Item):
            return self.name <= other.name
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Item):
            return self.name > other.name
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Item):
            return self.name >= other.name
        return NotImplemented