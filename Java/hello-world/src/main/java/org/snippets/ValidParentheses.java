package org.snippets;

import java.util.Map;
import java.util.Stack;

/**
 * Determine if a string of brackets such as (), {}, and []
 * is valid such that the brackets are balanced.
 */
public class ValidParentheses {

    public static void main(String[] args) {
        System.out.println("Valid Parentheses");
        String bracket = "(){}[]({})";
        boolean isBalanced = isValidBrackets(bracket);
        System.out.println(isBalanced);
    }

    static boolean isValidBrackets(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> closeToOpen = Map.of(
                ')', '(',
                '}', '{',
                ']', '['
        );
        for (char c : s.toCharArray()) {
            if (closeToOpen.containsKey(c)) {
                if (!stack.isEmpty() && stack.peek() == closeToOpen.get(c)) {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }
        return stack.isEmpty();
    }
}
