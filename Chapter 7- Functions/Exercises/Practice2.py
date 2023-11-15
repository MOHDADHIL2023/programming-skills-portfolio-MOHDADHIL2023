#Write a Python function that calculates the factorial of a given positive integer using recursion.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
result = factorial(5)
print(result)
