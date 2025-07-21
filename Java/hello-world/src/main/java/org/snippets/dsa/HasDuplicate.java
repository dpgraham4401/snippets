package org.snippets.dsa;

import java.util.HashSet;
import java.util.Set;

/**
 * Given an array of numbers, return true if the array has duplicates
 */
public class HasDuplicate {

    public static void main(String[] args) {
        int[] nums = {1, 2, 3};
        boolean hasDup = HasDuplicate.solution(nums);
        System.out.println(hasDup);
    }

    public static boolean solution(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (seen.contains(num)) {
                return true;
            }
            seen.add(num);
        }
        return false;
    }
}
