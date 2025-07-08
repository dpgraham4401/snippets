package org.snippets;

class NumberIsPrime {
    public static void main(String[] args) {
        assert isPrime(7);
        System.out.println("false: " + isPrime(6));
        System.out.println("false: " + isPrime(9));
        System.out.println("true: " + isPrime(5));
        System.out.println("true: " + isPrime(47));

    }

    static boolean isPrime(int input) {
        double squareRoot = Math.sqrt(input);
        int floorSquareRoot = (int) Math.floor(squareRoot);
        for (int i = 2; i <= floorSquareRoot; i++) {
            if (input % i == 0) {
                return false;
            }
        }
        return true;
    }
}