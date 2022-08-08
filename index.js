// Sandwich Machine by SoupHuman and electron271
//
// main.js

// Load the modules
const generate = require('./src/generate.js');
const prompt = require('prompt-sync')();

// Define sandwich types
console.log("sandwich-machine.github.io\nBy SoupHuman and electron271\n\n");

// Menu
console.log("Welcome to the Sandwich Machine!\n");
console.log("1. Generate a sandwich\n2. Quit\n");
// Get input
var input = prompt("Enter what you want to do: ");
// Switch on input
switch (input) {
    case "1":
        console.log("Generating Sandwich..\n");
        // Generate a sandwich
        generate.sandwichMenu();
        break;
    case "2":
        // Quit
        console.log("\nThanks for using the Sandwich Machine!\n");
        break;
    default:
        // Invalid input
        console.log("\nInvalid input!\n");
        break;
}
