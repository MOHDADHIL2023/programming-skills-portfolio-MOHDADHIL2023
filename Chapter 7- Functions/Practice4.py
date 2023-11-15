#Write a Python program that defines a function to calculate the area of a circle, and then
#calls that function with a given radius.


import math
def calculate_area(radius):
    area = math.pi * radius**2
    return area
radius = 5
area = calculate_area(radius)
print(f"The area of a circle with radius {radius} is {area}")
