/** Given a string, return a boolean indicating whether a string is a valid palindrome.
 * Palindromes are spelled the same backwards as forwards.
 * Ignore all non-alphanumeric characters.
 * This is as much a problem about how to use regex with javascript
 * as it is about being able to reverse and check a string
 */

const myValidPalindrome = "race car"
const nonPalindrome = "boobs"

function isPalindrome(value: string): boolean {
    const cleanedString = value.replace(/[^a-zA-Z0-9]/g, '')
    const reversedString = cleanedString.split('').reverse().join('')
    return reversedString === cleanedString
}

console.log(isPalindrome(myValidPalindrome));
console.log(isPalindrome(nonPalindrome));
