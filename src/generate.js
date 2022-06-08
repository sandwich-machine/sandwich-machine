// Sandwich Machine by SoupHuman and electron271
//
// src/generate.js

// Sandwich variables
var sandwichTypes = ["classic","grilled","double","bagel","burger"];

// Generate function
function sandwichSettings() {
    // Menu
    console.log("Sandwich settings\n");
    console.log("1. Output to console\n2. Log to file\n3. Quit\n");
    // Get input
    var input = prompt("Enter what you want to do: ");
    if (input == 1) {
        // Output to console
        console.log("\nYour sandwich will be a " + sandwichTypes[Math.floor(Math.random() * sandwichTypes.length)] + " sandwich.\n");
        // Run src/generate.js function sandwichSettings();
        sandwichSettings();
    } else if (input == 2) {
        // Log to file
        console.log("\nYour sandwich will be a " + sandwichTypes[Math.floor(Math.random() * sandwichTypes.length)] + " sandwich.\n");
        // Run src/generate.js function sandwichSettings();
        sandwichSettings();
    }
    else {
        // Quit
        console.log("\nThanks for using Sandwich Machine!\n");
        console.log("Have a nice day, and don't forget to eat a sandwich!\n");
        process.exit();
    }
}