// Sandwich Machine by SoupHuman and electron271
//
// src/generate.js

// load ./src/resources/ingredients.json
var ingredients = require('./resources/ingredients.json');

// Generate function
function generateSandwich() {
    // Menu
    console.log("Sandwich settings\n");
    console.log("1. Output to console\n2. Log to file\n3. Quit\n");
    // Get input
    var input = prompt("Enter what you want to do: ");
    // Switch on input
    switch (input) {
        case "1":
            // Output to console
            console.log("\nYour sandwich will be a " + sandwichTypes[Math.floor(Math.random() * sandwichTypes.length)] + " sandwich.\n");
            // Run src/generate.js function sandwichSettings();
            sandwichSettings();
            break;
        case "2":
            // Log to file
            console.log("\nYour sandwich will be a " + sandwichTypes[Math.floor(Math.random() * sandwichTypes.length)] + " sandwich.\n");
            // Run src/generate.js function sandwichSettings();
            sandwichSettings();
            break;
        case "3":
            // Quit
            console.log("\nThanks for using the Sandwich Machine!\n");
            break;
        default:
            // Invalid input
            console.log("\nInvalid input!\n");
    }
}