#Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, 
#move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ["BLT", "Turkey Club", "Grilled Cheese", "Ham and Cheese"]

finished_sandwiches = []

for order in sandwich_orders:
    print("I made your", order, "sandwich.")
    finished_sandwiches.append(order)

print("The following sandwiches were made:")
for sandwich in finished_sandwiches:
    print(sandwich)