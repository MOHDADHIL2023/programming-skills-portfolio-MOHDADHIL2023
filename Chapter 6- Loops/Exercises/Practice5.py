#Write a Python program that uses a while loop to find the largest number among a series of
#user-input values until they enter '0' to exit the loop.

largest = float('-inf')

while True:
    num = float(input("Enter a number (enter 0 to exit): "))
    
    if num == 0:
        break
    
    if num > largest:
        largest = num

print("The largest number is:", largest)
