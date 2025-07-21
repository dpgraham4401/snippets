package org.snippets.dsa;

import java.util.HashMap;

/**
 * Given two strings, return true if they're anagrams of each other, false otherwise.
 */
public class ValidAnagram {

    public static void main(String[] args) {
        int[] nums = {1, 2, 3};
        String s = "racecar";
        String t = "carrace";
        boolean isAnagram = ValidAnagram.solution(s, t);
        System.out.println(isAnagram);
    }

    public static boolean solution(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        HashMap<Character, Integer> sMap = new HashMap<>();
        HashMap<Character, Integer> tMap = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            sMap.put(s.charAt(i), sMap.getOrDefault(s.charAt(i), 0) + 1);
            tMap.put(t.charAt(i), tMap.getOrDefault(t.charAt(i), 0) + 1);
        }
        return sMap.equals(tMap);
    }
}
