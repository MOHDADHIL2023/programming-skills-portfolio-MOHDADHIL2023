#Write a Python program which accepts the radius of a circle from the user and compute the area.
import math 
radius = float(input("please enter the radius of the circle: "))
area = math.pi * radius**2
print("the area of the circle with radius", radius, "is:", area)
