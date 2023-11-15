#Write a Python program that defines a function to check whether a given number is prime

def is_prime(num): 
    if num <= 1: 
        return False 
    for i in range(2, int(num**0.5) + 1): 
        if num % i == 0: 
            return False 
        return True