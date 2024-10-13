# Distance Between Two Points
print("\nDistance Between Two Points")
x1 = float(input("Enter x1 coordinate: "))
y1 = float(input("Enter y1 coordinate: "))
x2 = float(input("Enter x2 coordinate: "))
y2 = float(input("Enter y2 coordinate: "))

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(
    f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f}"
)
