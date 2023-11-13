#Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a
#medium shirt with the default message, and a shirt of any size with a different message.

#creating a function called make_shirt() that accepts a size and the text of a message
def make_shirt(size="large",text="i love python"):
    print("size number of t-shirt",size)
    print("text number of t-shirt",text)
    
#calling the function
#shirts are large by default with a message that reads I love Python
make_shirt()

#medium shirt with the default message
make_shirt(size="medium")

#a shirt of any size with a different message.
make_shirt(size="medium",text="MAH")