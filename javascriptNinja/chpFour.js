/**
 * Secrets of a JavaScript Ninja - Chapter Four
 * - JavaScript functions for the journeyman
 */

// Every function is silently passed two parameters: `arguments` and `this`
// this represents the object context that the function was called in

function ninjaFunction() {
  console.log("this.foo:", this.foo);
}

// The context provided in `this` could be another function
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