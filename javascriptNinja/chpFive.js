/**
 * Secrets of the JavaScript Ninja
 * Chapter 5: Functions for the masters: closures and scopes
 */

// Simple closures
var outerValue = "samurai";
var later;
function outerFunction() {

    var innerValue = "ninja";

    function innerFunction() {
        console.log("Outer Value: " + outerValue);
        console.log("Inner Value: " + innerValue);
    }

    later = innerFunction;
}
outerFunction();

// Here, `later` remembers the scope that was present in innerFunction when it was created.
// Even though outerFunction has finished executing, innerFunction can still access outerValue and innerValue.
// It's like, we can use closures to as factories for functions that remember their environment.
later() // Outputs: outerValue: samurai, Inner Value: ninja

