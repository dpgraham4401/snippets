/**
 * Secrets of a JavaScript Ninja - Chapter Four
 * - JavaScript functions for the journeyman
 */

// Every function is silently passed two parameters: `arguments` and `this`
// this represents the object context that the function was called in

function ninjaFunction() {
  console.log("this.foo:", this.foo);
}

// The context provided in `this` could be another function (the one calling it)
function ninja() {
    this.foo = "baz";
    ninjaFunction(); 
}
ninja();

// It could also be an object
const myNina = {
    foo: "bar",
    ninjaFunction: ninjaFunction
};
myNina.ninjaFunction(); 

// Or it could be a class instance
class NinjaClass {
    constructor() {
        this.foo = "qux";
    }
    ninjaFunction() {
        console.log("this.foo:", this.foo);
    }
}
const myNinjaClass = new NinjaClass();
myNinjaClass.ninjaFunction();

// ARGUMENTS
// In addition to `this`, functions also have an `arguments` object
function ninjaWithArgs() {
    console.log("arguments:", arguments);
}
ninjaWithArgs(1, 2, 3, "foo", "bar");
// With the introduction of ES6 rest parameters, we don't need to use `arguments` as much
function ninjaWithRest(...args) {
    console.log("args:", args);
}
ninjaWithRest(1, 2, 3, "foo", "bar");


// Argument aliasing and the "use strict" directive
// If we change the values in `arguements`, it will change the values of the parameters
function ninjaWithAliasing(a, b) {
    // "use strict";
    console.log("Before:", a, b);
    arguments[0] = 10;
    arguments[1] = 20;
    console.log("After:", a, b);
}
ninjaWithAliasing(1, 2);
// We can prevent this behavior by using the "use strict" directive
// uncomment the "use strict" line, the arguments will not change

// The "use strict" directive has a few other semantics, like requiring parameters to be unique
// and some miscellaneous other things like use of `this`
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode

// Constructor Functions
// A constructor function is just a function that is called with the `new` keyword
// It typically is used to set up an object with properties via the `this` keyword

// When we call a function with the `new` keyword, it does the following:
// 1. Creates a new object
// 2. Implicitly pass the new empty object as `this`, executing the function in the context of that object
// 3. Return the new object (unless another object is returned, the new object will still be returned if we return a primitive).
function Ninja() {
    this.getThis = function() {
        return this;
    }
    this.foo = "ninja";
}

const ninja1 = new Ninja();
console.log(`${ninja1.getThis() === ninja1}`) // true
console.log(ninja1.foo); // "ninja"


// Explicitly setting the function's context with `call` and `apply`
const steve = {
    name: "steve"
}

function calculateUserDebt(...rest) {
    // We're using `this` but this function inherently has no property `name` in its context
    const debt = rest.reduce((accumulated, current) => accumulated + current);
    console.log(`Hello ${this.name}, you owe $${debt}`);
}
// `apply` accepts two args: the object to use as the context (`this`) and an array of arguments
calculateUserDebt.apply(steve, [1000, 2345, 719]); // Hello steve, you owe $4064

// `call` is basically identical except it accepts a list of arguments instead of an array
calculateUserDebt.call(steve, 100, 450, 20); // Hello steve, you owe $570


// Last, the `bing` method. This method is available to all functions, unlike `call` and `apply`
// It returns a new function that ALWAYS has the context of the object passed in as the first argument

const calculateSteveDebt = calculateUserDebt.bind(steve)
calculateSteveDebt(50, 25, 15, 10); // Hello steve, you owe $100

const joe = {
    // Notice our object has a different name property
    name: "joe",
    // because we used `bing`, `this` will still refer to `steve`
    calculateSteveDebt
}

joe.calculateSteveDebt(100, 200); // Hello steve, you owe $300

