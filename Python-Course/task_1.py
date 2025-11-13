# Create input prompts for the user to enter the number of lemons, sugar per cup, and base price.
# Store these values in variables using the input() function and ensure correct data types are used.
# Write code to calculate the total number of cups possible and the estimated revenue based on user input.
# Use arithmetic operators and variables to perform these calculations.
# Implement an if statement to check if the number of lemons is less than 5. If true, print a warning message to the user.

lemons = int(input("Enter thr number of lemons: "))

sugar_per_cup = float(input("Enter the amount of sugar per cup (in grams): "))

base_price = float(input("Enter the base price: "))

total_cups = lemons
revenue = total_cups * base_price

if lemons < 5:
    print("Warning: You have less than 5 lemons!")
else:
    print("You have plenty of lemons!")

print(f"Lemons: {lemons}\nSugar per cup: {sugar_per_cup}\nBase price: {base_price}\n")
print("Cups:", total_cups)
print("Estimated revenue:", revenue)
