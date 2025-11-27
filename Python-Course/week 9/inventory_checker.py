# Define the Item class with __str__ and __eq__ methods
class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} (x{self.quantity})"

    def __eq__(self, other):
        return self.name == other.name and self.quantity == other.quantity


# Set up inventory and added order list
inventory = {
    "apple": 10,
    "banana": 0,
    "orange": 5,
    "pear": 2,
    "grape": 20

}

