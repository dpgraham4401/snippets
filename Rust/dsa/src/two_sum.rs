//! Two sum
//! Given an array of numbers, and a target, return the indices of
//! two numbers from the array that sum to the target.
//! Assume there will always be 1 and only 1 solution.
//!

use std::collections::HashMap;

/// This implementation assumes that the nums are sorted
pub fn two_sum_sorted(nums: &[i32], target: i32) -> (i32, i32) {
    let mut l = 0;
    let mut r = nums.len() - 1;
    while l < r {
        let sum = nums[l] + nums[r];
        let m = l + (r - l) / 2;
        if sum > target {
            r = m;
        } else if sum < target {
            l = m;
        } else {
            break;
        }
    }
    (l as i32, r as i32)
}

/// This implementation assumes nums are not sorted
///
/// Notes:
///     Note the use of .iter().enumerate() to get the val and index.
///     The use of Some to get a potential value and in combo with `if let`
///     Last, the use of the `unreachable!` macro since we assume that there is at least 1 solution.
pub fn two_sum(nums: &[i32], target: i32) -> (i32, i32) {
    let mut index_map = HashMap::new();
    for (i, val) in nums.iter().enumerate() {
        let diff = target - val;
        if let Some(&j) = index_map.get(&diff) {
            return (j as i32, i as i32);
        }
        index_map.insert(val, i);
    }
    unreachable!("two_sum: no solution found");
}
