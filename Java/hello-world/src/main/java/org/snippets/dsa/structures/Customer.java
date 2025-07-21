package org.snippets.dsa.structures;

import java.util.ArrayList;

/**
 * Using the Comparable interface.
 * <p>
 * Many sorting utils in Java require us to be able to compare two instances
 * of a class to determine the order.
 */
public class Customer implements Comparable<Customer> {
    private final String name;

    public Customer(String name) {
        this.name = name;
    }

    @Override
    public int compareTo(Customer other) {
        return name.compareTo(other.name);
    }

    @Override
    public String toString() {
        return name;
    }
}
