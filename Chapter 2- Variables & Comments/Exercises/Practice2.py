#Write a python program that takes courses marks as input and then calculates average of all the
#courses. After calculating the average, calculate the percentage of a student using total marks. Assume
#the total of all the courses marks is 500 or take the total marks from the user as input. 

#creating input for course marks
course1 = float(input("Enter marks for course 1: "))
course2 = float(input("Enter marks for course 2: "))
course3 = float(input("Enter marks for course 3: "))
course4 = float(input("Enter marks for course 4: "))
course5 = float(input("Enter marks for course 5: "))

# Calculate average
average = (course1 + course2 + course3 + course4 + course5) / 5

# Calculate percentage
total_marks = 500
percentage = (average / total_marks) * 100

# Print the average and percentage
print("Average marks: ", average)
print("Percentage: ", percentage)