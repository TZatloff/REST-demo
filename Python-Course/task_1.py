# Create input prompts for the user to enter the number of lemons, sugar per cup, and base price.
# Store these values in variables using the input() function and ensure correct data types are used.
# Write code to calculate the total number of cups possible and the estimated revenue based on user input.
# Use arithmetic operators and variables to perform these calculations.
# Implement an if statement to check if the number of lemons is less than 5. If true, print a warning message to the user.
# Create a list of available lemonade flavors and a dictionary mapping each flavor to its price.
# Display these using print statements and f-strings.

lemons = int(input("Enter thr number of lemons: "))

sugar_per_cup = float(input("Enter the amount of sugar per cup (in grams): "))

price = float(input("Enter the price: "))

total_cups = lemons
revenue = total_cups * price

if lemons < 5:
    print("Warning: You have less than 5 lemons!")
else:
    print("You have plenty of lemons!")

flavors = ['classic', 'strawberry', 'mint']
flavor_prices = {
    'classic': 2.5,
    'strawberry': 3.0,
    'mint': 3.0
}

for flavor in flavors:
    print(f"{flavor}")
for flavor, price in flavor_prices.items():
    print(f"{flavor}: ${price}")

print(f"Lemons: {lemons}\nSugar per cup: {sugar_per_cup}\nBase price: {price}\n")
print("Cups:", total_cups)
print("Estimated revenue:", revenue)
