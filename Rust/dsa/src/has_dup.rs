//! Has Duplicates
//! Given an array of numbers, return true if the array contains a duplicate
//! return false otherwise.
//!

use std::collections::HashMap;

pub fn has_duplicate(nums: &[i32]) -> bool {
    let mut map = HashMap::new();
    let mut result = false;
    for num in nums {
        if map.contains_key(num) {
            result = true;
        } else {
            map.insert(num, true);
        }
    }
    println!("{:?} has duplicates: {}", nums, result);
    result
}
