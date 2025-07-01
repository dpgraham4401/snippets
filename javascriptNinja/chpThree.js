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

// not-important --> sleep function to simulate delay
const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

// We can use this to our advantage inside the function
// This function will memoize (read, cache) the results in memory
async function selfMemoizingFn(x) {
    if (!selfMemoizingFn.cache) {
        selfMemoizingFn.cache = {}
    }
    if (selfMemoizingFn.cache[x]) {
        return selfMemoizingFn.cache[x]
    }
    await sleep(1000)
    const result = x * 2
    selfMemoizingFn.cache[x] = result
    return result;
}

selfMemoizingFn(5).then(console.log); // 10, takes 1 second
selfMemoizingFn(5).then(console.log); // 10, but this time it's instant

// A 'function expression' is just when a function is used as part of another statement
const myFunction = function (x) {  // notice the lack of a name after 'function'
    return x * 2;
}
// The alternative (common) is just called a 'function declaration'
function aDeclaredFunction() {}