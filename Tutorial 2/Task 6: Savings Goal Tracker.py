# Savings Goal Tracker
print("\nSavings Goal Tracker")
target_savings = float(input("Enter your target savings goal: "))
current_savings = float(input("Enter your current savings amount: "))
monthly_savings = float(input("Enter your monthly saving amount: "))

months_to_reach_goal = (target_savings - current_savings) / monthly_savings
print(f"It will take you {months_to_reach_goal:.2f} months to reach your savings goal.")
