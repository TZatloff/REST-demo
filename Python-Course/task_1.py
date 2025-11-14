lemons = int(input("Enter thr number of lemons: "))

sugar_per_cup = float(input("Enter the amount of sugar per cup (in grams): "))

price = float(input("Enter the price: "))
# Developed prompts for user data entry and processing of entered values


total_cups = lemons
revenue = total_cups * price
# Implemented arithmetic calculations for cups and revenue

if lemons < 5:
    print("Warning: You have less than 5 lemons!")
else:
    print("You have plenty of lemons!")
# Added conditional warning for low lemons

print(f"Lemons: {lemons}\nSugar per cup: {sugar_per_cup}\nBase price: {price}\n")
print("Cups:", total_cups)
print("Estimated revenue:", revenue)

flavors = ['classic', 'strawberry', 'mint']
flavor_prices = {
    'classic': 2.5,
    'strawberry': 3.0,
    'mint': 3.0
}
print("Available flavors: ")
for flavor in flavors:
    print(f"{flavor}")

print("Prices for each flavors: ")
for flavor, price in flavor_prices.items():
    print(f"{flavor}: ${price}")
# Created a list of available lemonade flavors and a dictionary mapping each flavor,
# to its price and displayed them using f-string
