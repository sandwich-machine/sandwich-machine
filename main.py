print('Sandwich Machine')

from random import *
import os
import quality_control
types = [ 'classic', 'grilled', 'double', 'bagel', 'burger' ]
print('github.com/SoupDevHub/Sandwich-Machine\n')
print('''Menu
1. Generate a sandwich
2. Generate a sandwich (and output it to a file)
Please enter a option between 1-2 (not higher or lower, that may break our system)''')

option = input()

if option == "1":
    sandwichtype = choice(types)
    thing1 = choice(quality_control.qcthings(sandwichtype))
    thing2 = choice(quality_control.qcthings(sandwichtype))
    spread = choice(quality_control.qcspreads(sandwichtype))

    if sandwichtype == 'classic':
        print(f'''Type: Classic
        Step 1: Get two slices of bread.
        Step 2: Spread {spread.title()} on the bread.
        Step 3: Put {thing1} on one of the slices.
        Step 4: Put {thing2} on top of {thing1}.
        Step 5: Put the other slice on.''')
    elif sandwichtype == 'grilled':
        print(f'''Type: Grilled
        Step 1: Get two slices of bread.
        Step 2: Grill the bread.
        Step 3: Spread {spread.title()} on the bread.
        Step 4: Put {thing1} on one of the slices.
        Step 5: Put {thing2} on top of {thing1}.
        Step 6: Put the other slice on.''')
    elif sandwichtype == 'double':
        print(f'''Type: Double
        Step 1: Get three slices of bread.
        Step 2: Spread {spread.title()} on the bread.
        Step 3: Put {thing1} on two of the slices.
        Step 4: Put {thing2} on top of {thing1}.
        Step 5: Put the stacks on top of each other and put the other slice on.''')
    elif sandwichtype == 'bagel':
        print(f'''Type: Bagel
        Step 1: Slice a bagel.
        Step 2: Spread {spread.title()} on the bagel slices.
        Step 3: Put {thing1} on one of the slices.
        Step 4: Put {thing2} on top of {thing1}.
        Step 5: Put the other slice on.''')
    if sandwichtype == 'burger':
        print(f'''Type: Burger
        Step 1: Get two burger buns
        Step 2: Spread {spread.title()} on the bun.
        Step 3: Put {thing1} on one of the buns.
        Step 4: Put {thing2} on top of {thing1}.
        Step 5: Put the other bun on.''')
    print(f'I hope you enjoy your {thing1} and {thing2} {sandwichtype} sandwich with {spread}!')
if option == "2":
    print('How many sandwiches? (Too much may lag the system)')
    sandwiches = input()
    sandwiches = int(sandwiches)
    currentc = 0
    
    if os.path.exists("sandwiches.txt"):
        os.remove("sandwiches.txt")
    f = open('sandwiches.txt', 'x')
    while currentc < sandwiches:
        sandwichtype = choice(types)
        thing1 = choice(quality_control.qcthings(sandwichtype))
        thing2 = choice(quality_control.qcthings(sandwichtype))
        spread = choice(quality_control.qcspreads(sandwichtype))
        f = open('sandwiches.txt', 'a')
        f.write(f'I hope you enjoy your {thing1} and {thing2} {sandwichtype} sandwich with {spread}!\n')
        currentc+=1
    print("Finished outputting to sandwiches.txt! See it now!")

