// Sandwich Machine by SoupHuman and electron271
//
// main.js

// Load the modules
require("./generate.js");
require("./credits.js");


// Define sandwich types
console.log("sandwich-machine.github.io\nBy SoupHuman and electron271\n\n");

// Menu
console.log("Welcome to the Sandwich Machine!\n");
console.log("1. Generate a sandwich\n2. Credits\n3. Quit\n");
// Get input
var input = prompt("Enter what you want to do: ");
// Switch on input
switch (input) {
    case "1":
        // Generate a sandwich
        generate();
        break;
    case "2":
        // Show credits
        credits();
        break;
    case "3":
        // Quit
        console.log("\nThanks for using the Sandwich Machine!\n");
        break;
    default:
        // Invalid input
        console.log("\nInvalid input!\n");
}
