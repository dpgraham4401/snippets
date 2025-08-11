//! Rust FizzBuzz implementation
//!
//! Given a number n, print the numbers from 1 to n, unless the number is
//! a multiple of 3, in which case print "Fizz", or a multiple of 5,
//! in which case print "Buzz", or a multiple of both 3 and 5, in which case
//! print "FizzBuzz."

/// Notes:
///     instead of int, think of u32 as my default int (non-negative)
///     We don't need to supply a return type for a function that doesn't
///     return anything, but instead of `void`, we return `()`
///     using range iteration, use `=num` to iterate until `n <= num`,
///     using just `1..num` would iterate while `n < num`
pub fn fizzbuzz(num: u32) -> () {
    for n in 1..=num {
        if n % 3 == 0 && n % 5 == 0 {
            println!("FizzBuzz");
        } else if n % 3 == 0 {
            println!("Fizz");
        } else if n % 5 == 0 {
            println!("Buzz");
        } else {
            println!("{}", n);
        }
    }
}
