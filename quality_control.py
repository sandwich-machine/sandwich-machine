def qcthings(sandwichtype):
    if sandwichtype == 'classic': # If sandwich type is classic, give the list of ingredients below
        things = [ 'cheese', 'chicken', 'tuna', 'salmon', 'tomato', 'bacon', 'lettuce', 'turkey', 'pickle', 'olives', 'chili pepper', 'ham', 'avocado', 'cucumber', 'pepperoni', 'salami', 'steak', 'jelly' ]
    elif sandwichtype == 'grilled': # If sandwich type is grilled, give the list of ingredients below
        things = [ 'cheese', 'chicken', 'tuna', 'salmon', 'tomato', 'bacon', 'turkey', 'pickle', 'olives', 'chili pepper', 'ham', 'avocado', 'pepperoni', 'salami', 'steak' ]
    elif sandwichtype == 'double': # If sandwich type is double, give the list of ingredients below
        things = [ 'cheese', 'chicken', 'tuna', 'salmon', 'tomato', 'bacon', 'lettuce', 'turkey', 'pickle', 'olives', 'chili pepper', 'ham', 'avocado', 'cucumber', 'pepperoni', 'salami', 'steak', 'jelly' ]
    elif sandwichtype == 'bagel': # If sandwich type is bagel, give the list of ingredients below
        things = [ 'cheese', 'tomato', 'bacon', 'lettuce', 'ham', 'avocado', 'cucumber', 'pepperoni', 'salami', 'lox', 'onions', 'jelly', 'capers' ]
    elif sandwichtype == 'burger': # If sandwich type is burger, give the list of ingredients below
        things = [ 'cheese', 'chicken', 'tomato', 'bacon', 'lettuce', 'turkey', 'pickle', 'olives', 'chili pepper', 'cucumber', 'steak' ]
    else: # If the sandwich type is not defined here, set the ingredients to "error, sandwichtype not found"
        things = [ f'error, {sandwichtype} not found' ]
    return things # Return the ingredients

def qcspreads(sandwichtype):
    if sandwichtype == 'classic':  # If sandwich type is classic, give the list of spreads below
        spreads = [ 'nothing', 'mayo', 'peanut butter', 'avocado', 'honey', 'cream cheese' ]
    elif sandwichtype == 'grilled':  # If sandwich type is grilled, give the list of spreads below
        spreads = [ 'nothing', 'mayo', 'avocado', 'honey' ]
    elif sandwichtype == 'double':  # If sandwich type is double, give the list of spreads below
        spreads = [ 'nothing', 'mayo', 'peanut butter', 'avocado', 'honey', 'cream cheese' ]
    elif sandwichtype == 'bagel':  # If sandwich type is bagel, give the list of spreads below
        spreads = [ 'nothing', 'peanut butter', 'cream cheese', 'avocado' ]
    elif sandwichtype == 'burger':  # If sandwich type is burger, give the list of spreads below
        spreads = [ 'nothing', 'mayo', 'butter' ]
    else: # If the sandwich type is not defined here, set the spread to "error, sandwichtype not found"
        things = [ f'error, {sandwichtype} not found ' ]
    return spreads # Return the spreads


def pmthings(sandwichtype):
    things = [ 'cheese', 'chicken', 'tuna', 'salmon', 'tomato', 'bacon', 'lettuce', 'turkey', 'pickle', 'olives', 'chili pepper', 'ham', 'avocado', 'cucumber', 'pepperoni', 'salami', 'steak', 'jelly' ]
    
def pmspreads(sandwichtype):
    spreads = [ 'nothing', 'mayo', 'peanut butter', 'avocado', 'honey', 'cream cheese' ]
