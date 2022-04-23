print('Sandwich Machine by SoupDevHub and electron271') 

# Load modules and types
from random import *
import os
import quality_control
import recipe

types = [ 'classic', 'grilled', 'double', 'bagel', 'burger' ]
print('sandwich-machine.github.io\n') # Website

print('''------------------------------------------------
Menu
1. Generate a sandwich
2. Generate a sandwich (and output it to a file)
Please enter a option between 1-2
------------------------------------------------''') # Load Menu
option1 = input()
print('''\nSettings
1. Quality Control
2. Quality Control (With diets)
3. Pure Madness
Please enter a option between 1-3''')
option2 = input()

if option1 == '1': # Generate a sandwich
    sandwichtype = choice(types) # Get the type
    if option2 == '1':
        thing1 = choice(quality_control.qcthings(sandwichtype)) # Get thing1
        thing2 = choice(quality_control.qcthings(sandwichtype)) # Get thing2
        spread = choice(quality_control.qcspreads(sandwichtype)) # Get spread
    if option2 == '2':
        print('''\nDiets
        1. Vegetarian
        2. Vegan
        Please enter a option between 1-2''')
        option3 = input()
        if option2 == '1':
            thing1 = choice(quality_control.qcvtthings(sandwichtype)) # Get thing1
            thing2 = choice(quality_control.qcvtthings(sandwichtype)) # Get thing2
            spread = choice(quality_control.qcvtspreads(sandwichtype)) # Get spread
        if option2 == '2':
            thing1 = choice(quality_control.qcvthings(sandwichtype)) # Get thing1
            thing2 = choice(quality_control.qcvthings(sandwichtype)) # Get thing2
            spread = choice(quality_control.qcvspreads(sandwichtype)) # Get spread
    if option2 == '3':
        thing1 = choice(quality_control.pmthings(sandwichtype)) # Get thing1
        thing2 = choice(quality_control.pmthings(sandwichtype)) # Get thing2
        spread = choice(quality_control.pmspreads(sandwichtype)) # Get spread

    print(recipe.getrecipe(sandwichtype, thing1, thing2, spread)) # Get the recipe
    print(f'I hope you enjoy your {thing1} and {thing2} {sandwichtype} sandwich with {spread}!') # Output type
if option1 == '2': # Generate a sandwich (and output it to a file)
    print('How many sandwiches? (Too much may lag the system)') # Get how many sandwiches
    sandwiches = input() # Get input
    sandwiches = int(sandwiches) # Convert input to a integer
    currentc = 0
    
    if os.path.exists("sandwiches.txt"): # If sandwiches.txt exists, delete it!
        os.remove("sandwiches.txt")
    while currentc < sandwiches: # for all sandwiches, generate a sandwich and write to file
        sandwichtype = choice(types) # sandwichtype
        if option2 == '1':
            thing1 = choice(quality_control.qcthings(sandwichtype)) # get thing1
            thing2 = choice(quality_control.qcthings(sandwichtype)) # get thing2
            spread = choice(quality_control.qcspreads(sandwichtype)) # get spreads
        if option2 == '2':
            thing1 = choice(quality_control.pmthings(sandwichtype)) # Get thing1
            thing2 = choice(quality_control.pmthings(sandwichtype)) # Get thing2
            spread = choice(quality_control.pmspreads(sandwichtype)) # Get spread
        f = open('sandwiches.txt', 'a') # open sandwiches.txt
        f.write(recipe.getrecipe(sandwichtype, thing1, thing2, spread)) # get recipe and write it
        f.write(f'\nI hope you enjoy your {thing1} and {thing2} {sandwichtype} sandwich with {spread}!\n') # output type
        f.write('-----------------------------------------------\n') # line
        currentc+=1 # next sandwich
    f.write(f'sandwich-machine.github.io') # Add website to end of file
    print("Finished outputting to sandwiches.txt! See it now!") # confirmation

    print(recipe.getrecipe(sandwichtype, thing1, thing2, spread)) # Get the recipe
    print(f'I hope you enjoy your {thing1} and {thing2} {sandwichtype} sandwich with {spread}!') # Output type
