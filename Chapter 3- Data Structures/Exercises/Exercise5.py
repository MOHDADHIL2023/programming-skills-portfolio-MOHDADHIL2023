#You just heard that one of your guests can’t make the
#dinner, so you need to send out a new set of invitations. You’ll have to think of
#someone else to invite.
#•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
#•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#•Print a second set of invitation messages, one for each person who is still in your list.


Names=["Shakin","Fasial","Adil","Rashid","Zubair"]
print(f"{Names[2]} ,can't make it to the dinner tonight.")
Names[2]="Shihab"
print(f"Dear {Names[0]}, I invited to the dinner tonight at my place. Please don't be late!")
print(f"Dear {Names[1]}, I invited to the dinner tonight at my place. Please don't be late!")
print(f"Dear {Names[2]}, I invited to the dinner tonight at my place. Please don't be late!")
print(f"Dear {Names[3]}, I invited to the dinner tonight at my place. Please don't be late!")
print(f"Dear {Names[4]}, I invited to the dinner tonight at my place. Please don't be late!")