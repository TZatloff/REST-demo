# A simple budget calculator that takes user input for income and expenses,then calculates total expenses, remaining savings, and savings rate.

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

if total_expenses > income:
    print("Warning: Your expenses exceed your income!")

print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Savings: ${remaining_savings:.2f}")
print(f"Savings Rate: {savings_rate:.2f}%")
