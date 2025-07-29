/** Given a string, return a boolean indicating whether a string is a valid palindrome.
 * Palindromes are spelled the same backwards as forwards.
 * Ignore all non-alphanumeric characters.
 * This is as much a problem about how to use regex with javascript
 * as it is about being able to reverse and check a string
 */

const myValidPalindrome = "race car" // true
const nonPalindrome = "boobs" // false
const manPlanCanal = "A man, a plan, a canal, Panama!" // true

function isPalindrome(value: string): boolean {
    const cleanedString = value.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
    const reveredString = cleanedString.split('').reverse().join('')
    return reveredString === cleanedString;
}

function twoPointerForLoop(value: string): boolean {
    const cleanedString = value.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
    for (let i = 0, n = cleanedString.length - 1; i < n; i++, n--) {
        if (cleanedString[i] !== cleanedString[n]) {
            return false;
        }
    }
    return true;
}

function twoPointerWhileLoop(value: string): boolean {
    const cleanedString = value.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
    let l = 0, r = cleanedString.length - 1;
    while (l < r) {
        if (cleanedString[l] !== cleanedString[r]) {
            return false;
        }
        l++;
        r--;
    }
    return true;
}

function twoPointerWhileWithoutRegex(value: string): boolean {
    let l = 0, r = value.length - 1;
    while (l < r) {
        while (!value[l].match(/[a-zA-Z0-9]/g)) {
            l++;
        }
        while (!value[r].match(/[a-zA-Z0-9]/g)) {
            r--;
        }
        if (value[l].toLowerCase() !== value[r].toLowerCase()) {
            return false;
        }
        l++;
        r--;
    }
    return true;
}

console.log(twoPointerWhileWithoutRegex(myValidPalindrome));
console.log(twoPointerWhileWithoutRegex(nonPalindrome));
console.log(twoPointerWhileWithoutRegex(manPlanCanal));
