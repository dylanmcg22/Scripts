import math
pi = math.pi

radius = float(input("Enter a radius for a circle."))
area = pi * radius**2

print(f"A circle with a radius {radius} will have an area of %.2f." %area)