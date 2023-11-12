#A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
#* Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store 
#their meanings as values.
#* Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print 
#the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between 
#each word-meaning pair in your output.


glossary = {
    'variable': 'A container for a value that can be used throughout a program.',
    'function': 'A block of code that performs a specific task and can be called multiple times.',
    'loop': 'A control flow statement that allows code to be executed repeatedly.',
    'list': 'A collection of items that can be of different data types and can be modified.',
    'conditional': 'A statement that performs different actions based on whether a condition is true or false.'
}

for term, definition in glossary.items():
    print(f"{term.title()}: {definition}\n")