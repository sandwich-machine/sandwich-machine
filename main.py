print('Sandwich Machine')

from random import *
import os
import quality_control
types = [ 'classic', 'grilled', 'double', 'bagel' ]
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
        print(f'Type: Classic\nStep 1: Get two slices of bread.\nStep 2: Spread {spread.title()} on the bread.\nStep 3: Put {thing1} on one of the slices.\nStep 4: Put {thing2} on top of {thing1}.\nStep 5: Put the other slice on.')
    elif sandwichtype == 'grilled':
        print(f'Type: Grilled\nStep 1: Get two slices of bread.\nStep 2: Spread {spread.title()} on the bread.\nStep 3: Put {thing1} on one of the slices.\nStep 4: Put {thing2} on top of {thing1}.\nStep 5: Put the other slice on.\nStep 6: Grill the sandwich.')
    elif sandwichtype == 'double':
        print(f'Type: Double\nStep 1: Get three slices of bread.\nStep 2: Spread {spread.title()} on the bread.\nStep 3: Put {thing1} on two of the slices.\nStep 4: Put {thing2} on top of {thing1}.\nStep 5: Put the stacks on top of each other and put the other slice on.')
    elif sandwichtype == 'bagel':
        print(f'Type: Bagel\nStep 1: Slice a bagel.\nStep 2: Spread {spread.title()} on the bagel slices.\nStep 3: Put {thing1} on one of the slices.\nStep 4: Put {thing2} on top of {thing1}.\nStep 5: Put the other slice on.')
    elif sandwichtype == 'spaghetti':
        print(f'Type: Spaghetti\nStep 1: Get two spaghettis of spaghetti.\nStep 2: Spread {spread.title()} on the bread.\nStep 3: Put {thing1} on one of the spaghettis.\nStep 4: Put {thing2} on top of {thing1}.\nStep 5: Put the other spaghetti on.')
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

