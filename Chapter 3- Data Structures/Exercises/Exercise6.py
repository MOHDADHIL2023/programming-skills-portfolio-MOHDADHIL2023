#You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
#•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.
#•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#•Print a message to each of the two people still on your list, letting them know they’re still invited.
#•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

Names=["Shakin","Fasial","Adil","Rashid","Zubair"]
print(" sorry, i can invite only two peoples for dinner ")
while len(Names) > 2:
      Name = Names.pop()
print(f"Sorry {Name}, we can't invite you to dinner.")
print(f"{Names[0]} and {Names[1]}, you're still invited to dinner.")
del Names[0]
del Names[0]
print(Names)