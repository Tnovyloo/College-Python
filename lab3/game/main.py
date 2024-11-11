from classes import Resource, Product

if __name__ == '__main__':
    iron = Resource(name="Iron ore", price=3)
    coal = Resource(name="Coal", price=2)

    iron_ingot = Product(name="Iron ingot", price=50, required_items={iron: 5})
    steel_ingot = Product(name="Steel ingot", price=100, required_items={iron_ingot: 1, coal: 10})

    total_resources = steel_ingot.get_total_resources()
    for resource, quantity in total_resources.items():
        print(f"{resource.name}: {quantity}")