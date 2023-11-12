#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
#calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 
#to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.


glossary = {
    'list': 'A collection of items in a particular order.',
    'tuple': 'An immutable list.',
    'dictionary': 'A collection of key-value pairs.',
    'string': 'A series of characters.',
    'boolean': 'A value of either True or False.',
}

for key, value in glossary.items():
    print(f"{key.title()}: {value}")
    
glossary['loop'] = 'A programming construct that repeats a set of instructions until a specific condition is met.'
glossary['function'] = 'A named block of code designed to do a specific task.'
glossary['class'] = 'A blueprint for creating objects.'
glossary['module'] = 'A file containing Python definitions and statements.'
glossary['argument'] = 'A value passed to a function or method when it is called.'

for key, value in glossary.items():
    print(f"{key.title()}: {value}")