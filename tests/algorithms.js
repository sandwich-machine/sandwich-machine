import chalk from 'chalk';

// Export the function
module.exports = {
    testAlgorithms: testAlgorithms
}

// load ./src/resources/ingredients.json
var ingredients = require('../src/resources/ingredients.json');
// Load sandwich ingredients and types
var types = ingredients['quality-control'].types;
var thingsClassic = ingredients['quality-control'].things.classic;
var thingsGrilled = ingredients['quality-control'].things.grilled;
var thingsDouble = ingredients['quality-control'].things.double;
var thingsBagel = ingredients['quality-control'].things.bagel;
var thingsBurger = ingredients['quality-control'].things.burger;

// Load spreads
var spreadsClassic = ingredients['quality-control'].spreads.classic;
var spreadsGrilled = ingredients['quality-control'].spreads.grilled;
var spreadsDouble = ingredients['quality-control'].spreads.double;
var spreadsBagel = ingredients['quality-control'].spreads.bagel;
var spreadsBurger = ingredients['quality-control'].spreads.burger;

function testAlgorithms() {
    // Test sandwich generation algorithms
    var type = types[Math.floor(Math.random() * types.length)];
    console.log(chalk.blue('type: ' + type));
    switch (type) {
        case "classic":
            // Pick random thing from thingsClassic
            var thing1 = thingsClassic[Math.floor(Math.random() * thingsClassic.length)];
            var thing2 = thingsClassic[Math.floor(Math.random() * thingsClassic.length)];
            // Pick random spread from spreadsClassic
            var spread = spreadsClassic[Math.floor(Math.random() * spreadsClassic.length)];
            break;
        case "grilled":
            // Pick random thing from thingsGrilled
            var thing1 = thingsGrilled[Math.floor(Math.random() * thingsGrilled.length)];
            var thing2 = thingsGrilled[Math.floor(Math.random() * thingsGrilled.length)];
            // Pick random spread from spreadsGrilled
            var spread = spreadsGrilled[Math.floor(Math.random() * spreadsGrilled.length)];
            break;
        case "double":
            // Pick random thing from thingsDouble
            var thing1 = thingsDouble[Math.floor(Math.random() * thingsDouble.length)];
            var thing2 = thingsDouble[Math.floor(Math.random() * thingsDouble.length)];
            // Pick random spread from spreadsDouble
            var spread = spreadsDouble[Math.floor(Math.random() * spreadsDouble.length)];
            break;
        case "bagel":
            // Pick random thing from thingsBagel
            var thing1 = thingsBagel[Math.floor(Math.random() * thingsBagel.length)];
            var thing2 = thingsBagel[Math.floor(Math.random() * thingsBagel.length)];
            // Pick random spread from spreadsBagel
            var spread = spreadsBagel[Math.floor(Math.random() * spreadsBagel.length)];
            break;
        case "burger":
            // Pick random thing from thingsBurger
            var thing1 = thingsBurger[Math.floor(Math.random() * thingsBurger.length)];
            var thing2 = thingsBurger[Math.floor(Math.random() * thingsBurger.length)];
            // Pick random spread from spreadsBurger
            var spread = spreadsBurger[Math.floor(Math.random() * spreadsBurger.length)];
            break;
        default:
            // Invalid type
            console.error("Invalid type! The type was: " + type + "\nPlease make a issue on the GitHub repo.");
            break;
    }
    console.log(chalk.blue('thing1: ' + thing1));
    console.log(chalk.blue('thing2: ' + thing2));
    console.log(chalk.blue('spread: ' + spread));
}