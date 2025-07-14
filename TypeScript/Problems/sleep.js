/**
 * Example Problem: create a sleep function that takes a number of milliseconds.
 */

export async function sleep(ms) {
    // The trick here is simply create a new promise.
    // Promise constructor an 'executor', which is a function that accepts 2 callbacks
    // resolveFn, and rejectFn. Resolve is called (with the expected return value) to indicate success
    // rejectFn is called (with the error) to indicate failure.
    // Note, we don't define resolveFn, rejectFn.
    return new Promise( (resolve, reject) => {
        try {
            setTimeout(resolve, ms)
        } catch (error) {
            console.log(error.message)
            reject(error)
        }
    })
}


async function main() {
    console.log("hello")
    await sleep(1000)
    console.log("bye")
}
