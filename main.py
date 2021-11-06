print('Sandwich Machine by SoupDevHub and electron271') 

# Load modules and types
from random import *
import os
import quality_control
import recipe
import sys
import argparse

# Technical stuff
parser = argparse.ArgumentParser()
parser.add_argument('-g', '--ghactions', action='store_true')
args = parser.parse_args()
# Technical stuff end

types = [ 'classic', 'grilled', 'double', 'bagel', 'burger' ]
print('sandwich-machine.github.io\n') # Website

if args.ghactions:
    option = 2
    sandwiches = 7
    print('[DEBUG] Sucessful argument')
else:
    print('''Menu
    1. Generate a sandwich
    2. Generate a sandwich (and output it to a file)
    Please enter a option between 1-2 (not higher or lower, that may break our system)''') # Load Menu
    option = input()

if option == '1': # Generate a sandwich
    sandwichtype = choice(types) # Get the type
    thing1 = choice(quality_control.qcthings(sandwichtype)) # Get thing1
    thing2 = choice(quality_control.qcthings(sandwichtype)) # Get thing2
    spread = choice(quality_control.qcspreads(sandwichtype)) # Get spread

    print(recipe.getrecipe(sandwichtype, thing1, thing2, spread)) # Get the recipe
    print(f'I hope you enjoy your {thing1} and {thing2} {sandwichtype} sandwich with {spread}!') # Output type
if option == '2': # Generate a sandwich (and output it to a file)
    print('How many sandwiches? (Too much may lag the system)') # Get how many sandwiches
    sandwiches = input() # Get input 
    sandwiches = int(sandwiches) # Convert input to a integer
    currentc = 0
    
    if os.path.exists("sandwiches.txt"): # If sandwiches.txt exists, delete it!
        os.remove("sandwiches.txt")
    while currentc < sandwiches: # for all sandwiches, generate a sandwich and write to file
        sandwichtype = choice(types) # sandwichtype
        thing1 = choice(quality_control.qcthings(sandwichtype)) # get thing1
        thing2 = choice(quality_control.qcthings(sandwichtype)) # get thing2
        spread = choice(quality_control.qcspreads(sandwichtype)) # get spreads
        f = open('sandwiches.txt', 'a') # open sandwiches.txt
        f.write(recipe.getrecipe(sandwichtype, thing1, thing2, spread)) # get recipe and write it
        f.write(f'\nI hope you enjoy your {thing1} and {thing2} {sandwichtype} sandwich with {spread}!\n') # output type
        f.write('-----------------------------------------------\n') # line
        currentc+=1 # next sandwich
        print('[DEBUG] sandwich count: {}'.format(currentc))
    print("Finished outputting to sandwiches.txt! See it now!") # confirmation

