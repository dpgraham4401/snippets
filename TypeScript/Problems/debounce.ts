/**
 * A Debounce filter: If a function is called multiple times within the debounce filter's
 * time limit, it will cancel the original calls. It makes sure that a function is only
 * executed once after a period of inactivity.
 */

/**
 * As with a lot of these problems, we write a function that accepts another function
 * and hold some private state in the context of the returned function.
 *
 * The trick here is to use the return value of setTimeout, which is not something we always use.
 * setTimeout returns an integer, which is just an identifier to (called the 'timeout id') that we
 * can pass to clearTimeout to cancel the timer.
 */
function debounce(fn: (...args: any[]) => any, ms: number) {
    let timeout: null | number = null;

    return (...args: any[]) => {
        // If there is a timeout already set, cancel it so the previous call won't be executed
        if (timeout) {
            clearTimeout(timeout)
        }
        // Otherwise, set a timeout so fn(...args) is added to the event loop and executed after ms milliseconds
        timeout = setTimeout(() => {
            fn(...args)
        }, ms)
    }
}

const debouncedLog = debounce((msg) => console.log(msg), 500)

debouncedLog("foo")
debouncedLog("foobar")
debouncedLog("foobar...baz")
