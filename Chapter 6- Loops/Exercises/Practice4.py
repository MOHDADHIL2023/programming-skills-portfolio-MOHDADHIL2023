#Write a Python program that uses the break statement to exit a for loop when a specific
#condition is met.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 3 == 0:
        print(num)
        break
