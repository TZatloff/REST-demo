# PYCOR-32: Personal Budget Calculator

# PYCOR-33: Implement calculations for expenses, savings, and savings rate
income = float(input("Monthly income: "))
rent = float(input("Rent/Housing: "))
food = float(input("Food/Groceries: "))
fun = float(input("Fun/Other: "))

total_expenses = rent + food + fun
remaining_savings = income - total_expenses

if income > 0:
    savings_rate = (remaining_savings / income) * 100
else:
    savings_rate = 0

# PYCOR-34: Add conditional logic for overspending warning
if total_expenses > income:
    print("Warning: Your expenses exceed your income!")

# PYCOR-35: Format and display output using f-strings
print(f"\nTotal expenses: ${total_expenses:.2f}")
print(f"Remaining savings: ${remaining_savings:.2f}")
print(f"Savings rate: {savings_rate:.2f}%")
