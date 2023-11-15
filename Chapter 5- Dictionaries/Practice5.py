#Write a Python program to merge two dictionaries into one.

def M_D(D1, D2):
    return {**D1, **D2}
D1 = {'a': 1, 'b': 2}
D2 = {'c': 3, 'd': 4}
Merged_Dictionary =  M_D(D1, D2)
print(Merged_Dictionary)
