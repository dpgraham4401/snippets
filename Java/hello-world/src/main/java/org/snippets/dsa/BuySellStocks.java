package org.snippets.dsa;

/**
 * Given an array of integers, which represents the price of stocks through time,
 * determine the max profit one could make (the difference between the lowest and highest point).
 * If no positive difference, return 0.
 */
public class BuySellStocks {

    public static void main(String[] args) {
        int[] prices = {3, 4, 5, 7, 4, 3, 2, 1, 2, 3};
        int maxPrice = getMaxTransaction(prices);
        System.out.println(maxPrice);
    }

    /**
     * we need to store 3 values (2 of which are pointers), and the max transaction.
     * The pointers only move to the right, 1 just moves faster.
     * If the difference is greater than our current max transaction, store it keep going.
     * If the difference is negative (negative slope), move the left pointer.
     */
    public static int getMaxTransaction(int[] prices) {
        int l = 0, r = 1;
        int maxP = 0;
        while (r < prices.length) {
            int diff = prices[r] - prices[l];
            if (diff > maxP) {
                maxP = diff;
            }
            if (diff < 0) {
                l = r;
            }
            r++;
        }
        return maxP;
    }
}
