def qcthings(sandwichtype):
    if sandwichtype == 'classic': # If sandwich type is classic, give the list of ingredients below
        things = [ 'cheese', 'chicken', 'tuna', 'salmon', 'tomato', 'bacon', 'lettuce', 'turkey', 'pickle', 'olives', 'chili pepper', 'ham', 'avocado', 'cucumber', 'pepperoni', 'salami', 'steak' ]
    elif sandwichtype == 'grilled': # If sandwich type is grilled, give the list of ingredients below
        things = [ 'cheese', 'chicken', 'tuna', 'salmon', 'tomato', 'bacon', 'turkey', 'pickle', 'olives', 'chili pepper', 'ham', 'pepperoni', 'salami', 'steak' ]
    elif sandwichtype == 'double': # If sandwich type is double, give the list of ingredients below
        things = [ 'cheese', 'chicken', 'tuna', 'salmon', 'tomato', 'bacon', 'lettuce', 'turkey', 'pickle', 'olives', 'chili pepper', 'ham', 'cucumber', 'pepperoni', 'salami' ]
    elif sandwichtype == 'bagel': # If sandwich type is bagel, give the list of ingredients below
        things = [ 'cheese', 'tomato', 'bacon', 'lettuce', 'ham', 'avocado', 'cucumber', 'pepperoni', 'salami']
    elif sandwichtype == 'burger': # If sandwich type is burger, give the list of ingredients below
        things = [ 'cheese', 'chicken', 'tomato', 'bacon', 'lettuce', 'turkey', 'pickle', 'olives', 'chili pepper', 'cucumber', 'steak' ]
    else: # If the sandwich type is not defined here, set the ingredients to "error, sandwichtype not found"
        things = [ f'error, {sandwichtype} not found' ]
    return things # Return the ingredients

def qcspreads(sandwichtype):
    if sandwichtype == 'classic':  # If sandwich type is classic, give the list of spreads below
        spreads = [ 'mayo', 'peanut butter', 'avocado', 'jelly', 'honey' ]
    elif sandwichtype == 'grilled':  # If sandwich type is grilled, give the list of spreads below
        spreads = [ 'mayo', 'peanut butter', 'avocado', 'jelly', 'honey' ]
    elif sandwichtype == 'double':  # If sandwich type is double, give the list of spreads below
        spreads = [ 'mayo', 'peanut butter', 'jelly', 'honey' ]
    elif sandwichtype == 'bagel':  # If sandwich type is bagel, give the list of spreads below
        spreads = [ 'mayo', 'peanut butter', 'cream cheese', 'jelly', 'honey', 'avocado' ]
    elif sandwichtype == 'burger':  # If sandwich type is burger, give the list of spreads below
        spreads = [ 'mayo', 'cream cheese', 'honey' ]
    else: # If the sandwich type is not defined here, set the spread to "error, sandwichtype not found"
        things = [ f'error, {sandwichtype} not found ' ]
    return spreads # Return the spreads
