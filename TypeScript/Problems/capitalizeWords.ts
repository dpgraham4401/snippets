/**
 * Given a sentence (string), capitalize the first letter of each word
 */

function capitalizeWords(sentence: string): string {
    const tokens = sentence.split(' ');
    const capitalizedTokens = []
    for (let token of tokens) {
        capitalizedTokens.push(token.charAt(0).toUpperCase() + token.slice(1))
    }
    return capitalizedTokens.join(" ")
}


/**
 * This is the equivalent as the above, but is a JavaScript idiomatic version.
 * We split the sentence by spaces, create a new array but updating each word in the array
 * and join them again with a space.
 */
function shorterCapWords(sentence: string) {

    return sentence.split(" ")
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(" ")
}

const sentence = "Hello there, how's your day going?"

const capitalizedSentence = shorterCapWords(sentence);
console.log(capitalizedSentence)