/**
 * Example problem: write a function that accepts an array of strings and fetches all the URLs.
 * If one of the URLs fails, fail all of them
 */

async function fetchAll(urls: string[]) {
    const promises = Promise.all(urls.map((url => fetch(url)))).then(responses => {
        return Promise.all(responses.map(response => {
            return response.json();
        }))
    })
    return await promises
}

const numbers = Array.from({length: 100}, (_, i) => i + 1);
const URLs = numbers.map(num => `https://jsonplaceholder.typicode.com/todos/${num}`);

async function main() {
    const data = await fetchAll(URLs)
    console.log(data);
}

main();