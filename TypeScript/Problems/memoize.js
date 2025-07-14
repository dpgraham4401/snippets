/**
 * Memoization is a form of caching, we use JavaScript's closures to 
 * write a function (1), that accepts a function (2) and returns a new function (3).
 * The newly created function (3) has access to the lexical environment of our first function (1).
 * In that lexical env, we store a private object that stores the results, in memory, using the args as a key.
 * On future calls, if the args, as a key, is in the private object, we return that result instead of recomputing.
 */

import {sleep} from "./sleep.js";

function memoize(fn) {
    // It only lasts as along as the returned function (e.g., memoizedAdd) remains in memory.
    // It's good to keep in mind that it's not we're trading memory for CPU cycles
    const cache  = {}

    // We can use both an arrow fn or a fn declaration because we don't need access to 'this'
    // Arrow functions don't have their own 'this', they inherit it from whatever context they're defined in.
    return (...args) => {
        const key = args.toString();
        if (cache[key]) {
            return cache[key]
        }
        const result = fn(...args)
        cache[key] = result
        return result
    }
}

/**
 * A simple add function with an intentional delay added.
 */
async function add(x, y) {
    await sleep(500)
    return x + y;
}

const memoizedAdd = memoize(add)

console.time('First call');
console.log(await memoizedAdd(2, 3));
console.timeEnd('First call');

console.time('Second call');
console.log(await memoizedAdd(2, 3));
console.timeEnd('Second call');
