package org.snippets.dsa.structures;

import java.util.ArrayList;

/**
 * As we talked about in {@code  ./IterableInterfaceExamples}, the Collection interface extends the Iterable interface.
 * The Collection interface provides a lot of functionality,
 * just be aware of it, b/c I don't want to go over everything here.
 */
public class CollectionExamples {
    public static void main(String[] args) {
        ArrayList<String> myCollection = new ArrayList<>();
        java.util.Collections.addAll(myCollection, "a", "b", "c"); // instead of using .add("a") multiple times.
        System.out.println(myCollection);
        System.out.println(myCollection.isEmpty());
    }
}
