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
    let timeout: number | undefined;

    return (...args: any[]) => {
        if (timeout) {
            clearTimeout(timeout)
        }
        timeout = setTimeout(() => {
            fn(...args)
        }, ms)
    }
}

const debouncedLog = debounce((msg) => console.log(msg), 100)

debouncedLog("foo")
debouncedLog("bar")
debouncedLog("baz") // baz should be the only one logged
