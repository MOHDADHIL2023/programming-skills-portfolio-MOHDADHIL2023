#Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the
#owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about 
#each pet

pets = [
    {'animal': 'dog', 'owner': 'issac'},
    {'animal': 'cat', 'owner': 'yran'},
    {'animal': 'bird', 'owner': 'fasial'}
]

for pet in pets:
    print(f"{pet['owner']}'s pet is a {pet['animal']}.")