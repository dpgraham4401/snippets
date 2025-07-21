package org.snippets.dsa;

/**
 * Given a string, check that it is a palindrome.
 * A string that's spelled the same backwards as forwards.
 * disregard all non-alphanumeric characters (e.g., spaces).
 * Come up with a solution that operates in O(n) time and O(1) space.
 */
public class ValidPalindrome {

    public static void main(String[] args) {
        System.out.println("Valid Palindrome");
        String input = "0P";
        boolean isPalindrome = ValidPalindrome.isValidPalindrome(input);
        System.out.println(isPalindrome);
    }

    static boolean isValidPalindrome(String s) {
        String cleanedS = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        int l = 0;
        int r = cleanedS.length() - 1;
        while (l < r) {
            if (cleanedS.charAt(l) != cleanedS.charAt(r)) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}
