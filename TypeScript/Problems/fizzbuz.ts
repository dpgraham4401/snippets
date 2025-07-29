/**
 * FizzBuzz Problem
 * For multiples of three, print "Fizz" instead of the number.
 */

function fizzBuzz(n: number) {
    for (let i = 1; i <= n; i++) {
        let output = '';
        if (i % 3 == 0) output += "Fizz"
        if (i % 5 == 0) output += "Buzz"
        console.log(output || i)
    }
}

fizzBuzz(15)