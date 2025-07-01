/**
 * Chapter 3 - functions for novices
 * - functions as first class citizens (objects)
 */

// Functions can have properties assigned to them, just like objects
function foo(x) {
    const y = x
    return "foobar";
}
foo.bar = "Yo Momma!"

console.log(foo.bar);

