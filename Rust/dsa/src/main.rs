#![allow(dead_code)]

mod fizzbuzz;
mod has_dup;

fn main() {
    let nums = [1, 2, 3, 4, 5, 5];
    let nums2 = [1, 2, 3, 4, 5];

    has_dup::has_duplicate(&nums);
    has_dup::has_duplicate(&nums2);
}
