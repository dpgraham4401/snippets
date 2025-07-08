package org.snippets;

class ContainsVowel {
    public static void main(String[] args) {
        String input1 = "Fenster";
        String input2 = "TV";
        System.out.println(stringContainsVowel(input1));
        System.out.println(stringContainsVowel(input2));
        boolean output = stringContainsVowel("foo");
        assert output;
    }

    static boolean stringContainsVowel(String s) {
        return s.toLowerCase().matches(".*[aeiou].*");
    }
}
