// Module exports
module.exports = {
    getRecipe: getRecipe
}

function getRecipe(type, thing1, thing2, spread){
    switch (type) {
        case "classic":
            recipe = `Your sandwich type is Classic.
            Step 1: Get two slices of bread.
            Step 2: Put ${thing1} on the first slice of bread.
            Step 3: Put ${thing2} on top of the ${thing1}.
            Step 4: Spread ${spread} on top of the ${thing2}.
            Step 5: Put the second slice of bread on top of the ${spread}.
            Step 6 (optional): Cut your sandwich into TRIANGLES!
            Step 7: Enjoy your sandwich, and have a nice day! :)`;
            break;
        case "grilled":
            recipe = `Your sandwich type is Grilled.
            Step 1: Get two slices of bread.
            Step 2: Put ${thing1} on the first slice of bread.
            Step 3: Put ${thing2} on top of the ${thing1}.
            Step 4: Spread ${spread} on top of the ${thing2}.
            Step 5: Put the second slice of bread on top of the ${spread}.
            Step 6: Grill your sandwich.
            Step 7 (optional): Cut your sandwich into TRIANGLES!
            Step 8: Enjoy your sandwich, and have a nice day! :)`;
            break;
        case "double":
            recipe = `Your sandwich type is Double.
            Step 1: Get three slices of bread.
            Step 2: Put ${thing1} on two of the slices of bread.
            Step 3: Put ${thing2} on top of the ${thing1}.
            Step 4: Spread ${spread} on top of the ${thing2}.
            Step 5: Put the stacks on top of each other and put the other slice on.
            Step 6 (optional): Cut your sandwich into TRIANGLES!
            Step 7: Enjoy your sandwich, and have a nice day! :)`;
            break;
        case "bagel":
            recipe = `Your sandwich type is Bagel.
            Step 1: Slice a bagel.
            Step 2: Put ${thing1} on the bagel slice
            Step 3: Put ${thing2} on top of the ${thing1}.
            Step 4: Spread ${spread} on top of the ${thing2}.
            Step 5: Put the other slice on top of the ${spread}.
            Step 6: Enjoy your bagel, and have a nice day! :)`;
            break;
        case "burger":
            recipe = `Your sandwich type is Burger.
            Step 1: Get a burger bun.
            Step 2: Put ${thing1} on the first half of the bun.
            Step 3: Put ${thing2} on top of the ${thing1}.
            Step 4: Spread ${spread} on top of the ${thing2}.
            Step 5: Put the second half of the bun on top of the ${spread}.
            Step 6: Enjoy your burger, and have a nice day! :)`;
            break;
    }
    return recipe;
}
