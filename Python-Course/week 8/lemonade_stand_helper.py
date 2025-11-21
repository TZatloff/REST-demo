# PYCOR-23: Lemonade Stand Helper

# PYCOR-24: Design user input prompts and handle input values
lemons = int(input("Enter the number of lemons: "))
sugar_per_cup = float(input("Enter the amount of sugar per cup (in grams): "))
price = float(input("Enter the price per cup: "))

# PYCOR-25: Implement arithmetic calculations for cups and revenue
total_cups = lemons
revenue = total_cups * price

# PYCOR-26: Add conditional warning for low lemons
if lemons < 5:
    print("Warning: You have less than 5 lemons!")
else:
    print("You have plenty of lemons.")

# PYCOR-28: Format and print output as per example
print(f"\nLemons: {lemons}")
print(f"Sugar per cup: {sugar_per_cup} g")
print(f"Base price: ${price:.2f}")
print(f"Cups: {total_cups}")
print(f"Estimated revenue: ${revenue:.2f}\n")

# PYCOR-27: Define and display available flavors and prices
flavors = ["classic", "strawberry", "mint"]
flavor_prices = {
    "classic": 2.5,
    "strawberry": 3.0,
    "mint": 3.0,
}

print("Available flavors:")
for flavor in flavors:
    print(f"- {flavor.title()}")

print("\nPrices for each flavor:")
for flavor, flavor_price in flavor_prices.items():
    print(f"{flavor.title()}: ${flavor_price:.2f}")
