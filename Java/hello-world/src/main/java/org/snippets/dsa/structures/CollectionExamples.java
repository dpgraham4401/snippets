package org.snippets.dsa.structures;

import java.util.ArrayList;
import java.util.List;

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
        usingLists();
    }

    public static void usingLists() {
        List<String> list = new ArrayList<String>();
        java.util.Collections.addAll(list, "foo", "bar", "quq", "bar", "baz");
        System.out.println(list.indexOf("foo"));
        System.out.println(list.indexOf("asdf"));
        System.out.println(list.lastIndexOf("bar"));
        System.out.println(list.subList(0, 2)); // 0 up to (but not including) index 2
    }
}
