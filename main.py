print('Sandwich Machine')

from random import *
import os
import quality_control
import recipe
types = [ 'classic', 'grilled', 'double', 'bagel', 'burger' ]
print('sandwich-machine.github.io\n')
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

    print(recipe.getrecipe(sandwichtype, thing1, thing2, spread))
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
        f.write(recipe.getrecipe(sandwichtype, thing1, thing2, spread))
        f.write(f'\nI hope you enjoy your {thing1} and {thing2} {sandwichtype} sandwich with {spread}!\n')
        f.write('-----------------------------------------------\n')
        currentc+=1
    print("Finished outputting to sandwiches.txt! See it now!")

