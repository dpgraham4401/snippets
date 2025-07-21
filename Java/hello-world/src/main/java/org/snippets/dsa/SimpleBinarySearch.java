package org.snippets.dsa;

/**
 * Given an array of distinct integers, sorted in ascending order, and a target value,
 * implement a search function that returns it's index or -1 if the target is not found.
 */
public class SimpleBinarySearch {

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        int target = 8;
        int result = binarySearch(arr, target);
        System.out.println("Index of " + target + ": " + result);
    }

    public static int binarySearch(int[] nums, int target) {
        int l = 0;
        int r = nums.length - 1;

        while (l <= r) {
            int m = l + ((r - l) / 2);
            if (nums[m] > target) {
                r = m - 1;
            } else if (nums[m] < target) {
                l = m + 1;
            } else if (nums[m] == target) {
                return m;
            }
        }
        return -1;
    }
}
