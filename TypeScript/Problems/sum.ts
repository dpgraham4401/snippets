/**
 * Using the reduce method, write a function that takes an array 
 * of numbers and returns the sum of all the numbers in the array.
 */

function sumEmUp(numbers: number[]): number {
    return numbers.reduce((accumulator, num) => accumulator + num )
}

const myNumbers = [1, 2, 3, 4]

console.log(sumEmUp(myNumbers));
