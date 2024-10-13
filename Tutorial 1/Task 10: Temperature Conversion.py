# Temperature Conversion Program
choice = input("Type 'C' to convert Celsius to Fahrenheit or 'F' to convert Fahrenheit to Celsius: ").upper()

if choice == 'C':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is {fahrenheit}°F")
elif choice == 'F':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is {celsius}°C")
else:
    print("Invalid input.")
