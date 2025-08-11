#![allow(dead_code)]

mod fizzbuzz;
mod has_dup;
mod two_sum;

fn main() {
    let nums = [1, 2, 3, 4, 5, 5];
    let indices = two_sum::two_sum(&nums, 9);
    println!("{:?}", indices);
}
