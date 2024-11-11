from .item import Item

class Resource(Item):
    def get_info(self):
        return f"Resource: {self.name}\nPrice: {self.price}"
    