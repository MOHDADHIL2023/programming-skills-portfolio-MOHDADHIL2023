#Write a Python program which accepts the radius of a circle from the user and compute the area.
import math
Radius = float(input("Please Enter The Radius Of The Circle; "))
Area = math.pi * Radius**2
print("The Area Of The Circle With Radius" , Radius, "is:", Area)