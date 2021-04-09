print('Sandwich Machene')
from random import *
print('Random Sandwiches')



types = ['classic', 'grilled', 'double', 'bagel']

if choice(types) == 'classic':
    print('Type: Classic')
elif choice(types) == 'grilled':
    print('Type: Grilled')
elif choice(types) == 'double':
    print('Type: Double Decker')
elif choice(types) == 'bagel':
    print('Type: Bagel')

print('I hope you enjoy your sandwich!')
