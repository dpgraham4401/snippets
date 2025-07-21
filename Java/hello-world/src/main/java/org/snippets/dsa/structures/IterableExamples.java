package org.snippets.dsa.structures;

import java.util.Iterator;

/**
 * Java Collections framework.
 * <p>
 * The Collections framework includes a number of interfaces and concrete classes.
 * The Collection interface extends the Iterable interface, and there are over 20 concrete implementations.
 * There are three sub interfaces of the Collection interface, List, Queue, and Set.
 * There are various concrete classes in the std lib of these three interfaces, such as
 * ArrayList, LinkedList, PriorityQueue, and HasSet.
 */
public class IterableExamples {

    public static void main(String[] args) {
        String[] myList = {"foo", "bar", "baz"};
        Iterable<String> myIter = new MyIterableClass(myList);
        for (String item : myIter) {
            System.out.println(item);
        }
    }
}

/**
 * We can create custom iterable classes by implementing the Iterable interface.
 * This means we need to implement the required `iterator` method, which is
 * typically implemented by creating an inner, private, class. That class implements the
 * Iterator interface and returns a new instance of this private Iterator.
 */
class MyIterableClass implements Iterable<String> {
    private final String[] items;

    public MyIterableClass(String[] items) {
        this.items = items;
    }

    @Override
    public Iterator<String> iterator() {
        return new MyListIterator<>(items);
    }

    private class MyListIterator<T> implements Iterator<T> {
        private final T[] items;
        private int index;

        public MyListIterator(T[] items) {
            this.items = items;
        }

        @Override
        public boolean hasNext() {
            return (index < items.length);
        }

        @Override
        public T next() {
            return items[index++];
        }
    }

}