/**
 * Write a higher level function that accepts an async function and retries X number of timesjk
 */

async function retry<T>(fn: () => Promise<T>, retries: number): Promise<T> {
    try {
        return await fn();
    } catch (error) {
        if (retries > 0){
            console.log(`Retrying: ${retries}`)
            return retry(fn, retries - 1)
        } else {
            console.log("Max retries reached")
            throw error;
        }
    }
}

const failingFn = async () => {
  throw new Error("intended error")
}

retry(failingFn, 5)
