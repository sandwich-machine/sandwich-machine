print('Sandwich Machine')
from random import *
print('Random Sandwiches')


types = [ 'classic', 'grilled', 'double', 'bagel' ]
spreads = [ 'spaghetti', 'spaghetti', 'spaghetti', 'spaghetti', 'spaghetti', 'spaghetti', 'spaghetti', 'spaghetti', 'spaghett>
t1 = [ 'spaghetti', 'spaghetti', 'spaghetti', 'spaghetti', 'spaghetti', 'spaghetti', 'spaghetti', 'spaghetti', 'spaghetti', '>
t2 = [ 'spaghetti', 'spaghetti', 'spaghetti', 'spaghetti', 'spaghetti', 'spaghetti', 'spaghetti', 'spaghetti', 'spaghetti', '>


thing1 = choice(t1)
thing2 = choice(t2)
spread = choice(spreads)
type = choice(types)

if type == 'classic':
    print(f'Type: Classic\nStep 1: Get two slices of bread.\nStep 2: {spread.title()} the bread.\nStep 3: Put {thing1} on one>
elif type == 'grilled':
    print(f'Type: Grilled\nStep 1: Get two slices of bread.\nStep 2: {spread.title()} the bread.\nStep 3: Put {thing1} on one>
elif type == 'double':
    print(f'Type: Double\nStep 1: Get three slices of bread.\nStep 2: {spread.title()} the bread.\nStep 3: Put {thing1} on tw>
elif type == 'bagel':
    print(f'Type: Bagel\nStep 1: Slice a bagel.\nStep 2: {spread.title()} the bagel slices.\nStep 3: Put {thing1} on one of t>
print(f'I hope you enjoy your {thing1} and {thing2} {type} sandwich!')
