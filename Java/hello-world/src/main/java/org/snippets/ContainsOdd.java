package org.snippets;

import java.util.List;

/**
 * Given an array of integers, return true if one of the numbers is odd.
 */
class ContainsOdd {
    public static void main(String[] args) {
        Integer[] myNumbers = {2, 4};
        List<Integer> myNums = List.of(myNumbers);
        boolean hasOdd = containsOdd(myNums);
        System.out.println(hasOdd);
    }

    static boolean containsOdd(Iterable<Integer> numbers) {
        for (int num : numbers) {
            if (num % 2 != 0) {
                return true;
            }
        }
        return false;
    }

}