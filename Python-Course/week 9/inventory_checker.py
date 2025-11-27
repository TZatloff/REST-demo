# Define the Item class with __str__ and __eq__ methods
class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} (x{self.quantity})"

    def __eq__(self, other):
        return self.name == other.name and self.quantity == other.quantity


item = Item("Apple", 10)
print(str(item))
