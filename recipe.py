def getrecipe(sandwichtype, thing1, thing2, spread):
    if sandwichtype == 'classic':
        recipe = f'''Type: Classic
        Step 1: Get two slices of bread.
        Step 2: Spread {spread.title()} on the bread.
        Step 3: Put {thing1} on one of the slices.
        Step 4: Put {thing2} on top of {thing1}.
        Step 5: Put the other slice on.
        Step 6: Cut it into TRIANGLES! (superior sandwich shape)'''
    elif sandwichtype == 'grilled':
        recipe = f'''Type: Grilled
        Step 1: Get two slices of bread.
        Step 2: Spread {spread.title()} on the bread.
        Step 3: Put {thing1} on one of the slices.
        Step 4: Put {thing2} on top of {thing1}.
        Step 5: Put the other slice on.
        Step 6: Grill the sandwich
        Step 7: Cut it into TRIANGLES! (superior sandwich shape)'''
    elif sandwichtype == 'double':
        recipe = f'''Type: Double
        Step 1: Get three slices of bread.
        Step 2: Spread {spread.title()} on the bread.
        Step 3: Put {thing1} on two of the slices.
        Step 4: Put {thing2} on top of {thing1}.
        Step 5: Put the stacks on top of each other and put the other slice on.
        Step 6: Cut it into TRIANGLES! (superior sandwich shape)'''
    elif sandwichtype == 'bagel':
        recipe = f'''Type: Bagel
        Step 1: Slice a bagel.
        Step 2: Spread {spread.title()} on the bagel slices.
        Step 3: Put {thing1} on one of the slices.
        Step 4: Put {thing2} on top of {thing1}.
        Step 5: Put the other slice on.'''
    if sandwichtype == 'burger':
        recipe = f'''Type: Burger
        Step 1: Get two burger buns
        Step 2: Spread {spread.title()} on the bun.
        Step 3: Put {thing1} on one of the buns.
        Step 4: Put {thing2} on top of {thing1}.
        Step 5: Put the other bun on.'''
    return recipe
