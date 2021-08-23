print('Sandwich Machine')

from random import *
import os
types = [ 'classic', 'grilled', 'double', 'bagel' ]
spreads = [ 'mayo', 'butter', 'peanut butter', 'avocado', 'cream cheese' ]
t1 = [ 'cheese', 'tomato', 'bacon', 'lettuce', 'turkey', 'pickle', 'olives', 'chili pepper', 'ham', 'jelly', 'honey', 'avocado', 'cucumber', 'pepperoni', 'salami', 'steak' ]
t2 = [ 'cheese', 'tomato', 'bacon', 'lettuce', 'turkey', 'pickle', 'olives', 'chili pepper', 'ham', 'jelly', 'honey', 'avocado', 'cucumber', 'pepperoni', 'salami', 'steak' ]
print('github.com/SoupDevHub/Sandwich-Machine\n')
print('''Menu
1. Generate a sandwich
2. Generate a sandwich (and output it to a file)
Please enter a option between 1-2 (not higher or lower, that may break our system)''')

option = input()

if option == "1":
    thing1 = choice(t1)
    thing2 = choice(t2)
    spread = choice(spreads)
    sandwichtype = choice(types)

    if sandwichtype == 'classic':
        print(f'Type: Classic\nStep 1: Get two slices of bread.\nStep 2: Spread {spread.title()} on the bread.\nStep 3: Put {thing1} on one of the slices.\nStep 4: Put {thing2} on top of {thing1}.\nStep 5: Put the other slice on.')
    elif sandwichtype == 'grilled':
        print(f'Type: Grilled\nStep 1: Get two slices of bread.\nStep 2: Spread {spread.title()} on the bread.\nStep 3: Put {thing1} on one of the slices.\nStep 4: Put {thing2} on top of {thing1}.\nStep 5: Put the other slice on.\nStep 6: Grill the sandwich.')
    elif sandwichtype == 'double':
        print(f'Type: Double\nStep 1: Get three slices of bread.\nStep 2: Spread {spread.title()} on the bread.\nStep 3: Put {thing1} on two of the slices.\nStep 4: Put {thing2} on top of {thing1}.\nStep 5: Put the stacks on top of each other and put the other slice on.')
    elif sandwichtype == 'bagel':
        print(f'Type: Bagel\nStep 1: Slice a bagel.\nStep 2: Spread {spread.title()} on the bagel slices.\nStep 3: Put {thing1} on one of the slices.\nStep 4: Put {thing2} on top of {thing1}.\nStep 5: Put the other slice on.')
if option == "2":
    print('How many sandwiches? (Too much may lag the system)')
    sandwiches = input()
    sandwiches = int(sandwiches)
    currentc = 0
    
    if os.path.exists("sandwiches.txt"):
        os.remove("sandwiches.txt")
    f = open('sandwiches.txt', 'x')
    while currentc < sandwiches:
        thing1 = choice(t1)
        thing2 = choice(t2)
        spread = choice(spreads)
        sandwichtype = choice(types)
        f = open('sandwiches.txt', 'a')
        f.write(f'I hope you enjoy your {thing1} and {thing2} {sandwichtype} sandwich with {spread}!\n')
        currentc+=1
    print("Finished outputting to sandwiches.txt! See it now!")

