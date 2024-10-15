# Tax Calculator Program

# Get the gross income from the user
gross_income = float(input("Enter your gross income: £"))

# Initialize tax owed to 0
tax_owed = 0.0

# Determine the tax bracket and calculate the tax
if gross_income <= 12500:
    tax_owed = 0.0
elif gross_income <= 50000:
    tax_owed = (gross_income - 12500) * 0.20
elif gross_income <= 150000:
    tax_owed = (50000 - 12500) * 0.20 + (gross_income - 50000) * 0.40
else:
    tax_owed = (50000 - 12500) * 0.20 + (150000 - 50000) * 0.40 + (gross_income - 150000) * 0.45

# Calculate net income
net_income = gross_income - tax_owed

# Display the results
print(f"Tax owed: £{tax_owed:.2f}")
print(f"Net income: £{net_income:.2f}")
