print('Sandwich Machine')

from random import *
import os
import quality_control_gh_actions as quality_control
types = [ 'classic', 'grilled', 'double', 'bagel' ]
print('github.com/SoupDevHub/Sandwich-Machine\n')
print('How many sandwiches? (Too much may lag the system)')
sandwiches = 5
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
