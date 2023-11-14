#Write a Python program that uses the elif statement to determine the season based on the
#month provided as input.

month = input("Enter The Month: ")

if month == "December" or month == "January" or month == "February":
    season = "winter"
elif month == "March" or month == "April" or month == "May":
    season = "Spring"
elif month == "June" or month == "July" or month == "August":
    season = "Summer"
elif month == "September" or month == "October" or month == "November":
    season = "Autumn"
else:
    season = "month"

print("the season for",month,"is",season)