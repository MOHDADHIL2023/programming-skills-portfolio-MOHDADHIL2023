#Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function 
#should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional 
#arguments to make a shirt. Call the function a second time using keyword arguments.

#creating a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt
def make_shirt(size,text):
    print("size in t-shirt:",size)
    print("text in t-shirt:",text)

#calling the function

#positional arguments
make_shirt("medium","not at all")

#keyword arguments
make_shirt(text="never give up",size="large")
