package org.snippets;

/**
 * Given a string, reverse it
 */
public class ReverseAString {
    public static void main(String[] args) {
        String input = "foobar";
        String output = reverseString(input);
        System.out.println(output);
        assert output.equals("raboof");
    }

    static String reverseString(String s) {
        StringBuilder output = new StringBuilder();
        char[] chars = s.toCharArray();
        for (int i = chars.length - 1; i >= 0; i--) {
            output.append(chars[i]);
        }
        return output.toString();
    }
}
