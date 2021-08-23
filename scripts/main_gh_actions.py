print('Sandwich Machine')

from random import *
import os
import quality_control_gh_actions as quality_control
types = [ 'classic', 'grilled', 'double', 'bagel', 'burger' ]
print('github.com/SoupDevHub/Sandwich-Machine\n')

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