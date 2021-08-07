print('Sandwich Machine')
from random import *
print('Random Sandwiches')

types = [ 'classic', 'grilled', 'double', 'bagel', 'spaghetti' ]
spreads = [ 'mayo', 'butter', 'spaghetti', 'peanut butter' ]
t1 = [ 'cheese', 'tomato', 'bacon', 'lettuce', 'turkey', 'pickle', 'olives' , 'spaghetti', 'chili pepper', 'ham', 'jelly', 'honey', 'avocado', 'cucumber' ]
t2 = [ 'cheese', 'tomato', 'bacon', 'lettuce', 'turkey', 'pickle', 'olives' , 'spaghetti', 'chili pepper', 'ham', 'jelly', 'honey', 'avocado', 'cucumber' ]

thing1 = choice(t1)
thing2 = choice(t2)
spread = choice(spreads)
type = choice(types)

if type == 'classic':
    print(f'Type: Classic\nStep 1: Get two slices of bread.\nStep 2: Spread {spread.title()} on the bread.\nStep 3: Put {thing1} on one of the slices.\nStep 4: Put {thing2} on top of {thing1}.\nStep 5: Put the other slice on.')
elif type == 'grilled':
    print(f'Type: Grilled\nStep 1: Get two slices of bread.\nStep 2: Spread {spread.title()} on the bread.\nStep 3: Put {thing1} on one of the slices.\nStep 4: Put {thing2} on top of {thing1}.\nStep 5: Put the other slice on.\nStep 6: Grill the sandwich.')
elif type == 'double':
    print(f'Type: Double\nStep 1: Get three slices of bread.\nStep 2: Spread {spread.title()} on the bread.\nStep 3: Put {thing1} on two of the slices.\nStep 4: Put {thing2} on top of {thing1}.\nStep 5: Put the stacks on top of each other and put the other slice on.')
elif type == 'bagel':
    print(f'Type: Bagel\nStep 1: Slice a bagel.\nStep 2: Spread {spread.title()} on the bread.\nStep 3: Put {thing1} on one of the slices.\nStep 4: Put {thing2} on top of {thing1}.\nStep 5: Put the other slice on.')
elif type == 'spaghetti':
    print(f'Type: Spaghetti\nStep 1: Get two spaghettis of spaghetti.\nStep 2: Spread {spread.title()} on the bread.\nStep 3: Put {thing1} on one of the spaghettis.\nStep 4: Put {thing2} on top of {thing1}.\nStep 5: Put the other spaghetti on.')
print(f'I hope you enjoy your {thing1} and {thing2} {type} sandwich!')
