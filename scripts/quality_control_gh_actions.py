def qcthings(sandwichtype):
    if sandwichtype == 'classic':
        things = [ 'cheese', 'tuna', 'salmon', 'tomato', 'bacon', 'lettuce', 'turkey', 'pickle', 'olives', 'chili pepper', 'ham', 'avocado', 'cucumber', 'pepperoni', 'salami', 'steak' ]
    elif sandwichtype == 'grilled':
        things = [ 'cheese', 'tuna', 'salmon', 'tomato', 'bacon', 'turkey', 'pickle', 'olives', 'chili pepper', 'ham', 'pepperoni', 'salami', 'steak' ]
    elif sandwichtype == 'double':
        things = [ 'cheese', 'tuna', 'salmon', 'tomato', 'bacon', 'lettuce', 'turkey', 'pickle', 'olives', 'chili pepper', 'ham', 'cucumber', 'pepperoni', 'salami' ]
    elif sandwichtype == 'bagel':
        things = [ 'cheese', 'tomato', 'bacon', 'lettuce', 'ham', 'avocado', 'cucumber', 'pepperoni', 'salami']
    if sandwichtype == 'burger':
        things = [ 'cheese', 'tomato', 'bacon', 'lettuce', 'turkey', 'pickle', 'olives', 'chili pepper', 'cucumber', 'steak' ]
    else:
        things = [ f'error, {sandwichtype} not found ' ]
    return things

def qcspreads(sandwichtype):
    if sandwichtype == 'classic':
        spreads = [ 'mayo', 'peanut butter', 'avocado', 'jelly', 'honey' ]
    elif sandwichtype == 'grilled':
        spreads = [ 'mayo', 'peanut butter', 'avocado', 'jelly', 'honey' ]
    elif sandwichtype == 'double':
        spreads = [ 'mayo', 'peanut butter', 'jelly', 'honey' ]
    elif sandwichtype == 'bagel':
        spreads = [ 'mayo', 'peanut butter', 'cream cheese', 'jelly', 'honey', 'avocado' ]
    elif sandwichtype == 'burger':
        spreads = [ 'mayo', 'cream cheese', 'honey' ]
    else:
        things = [ f'error, {sandwichtype} not found ' ]
    return spreads