package org.example;
// Java packages often follow a reverse domain

// we can import classes following a dot style notation

import org.foo.Foo;

// The 'Main' class (note capitalization) has special significance
public class Main {
    // The main method of the Main class is also special
    public static void main(String[] args) {
        // 'static' class methods can be called without instantiating
        Foo.sayFoo(true);
        // To instantiate a new object: <ClassName> <VarName> = new <ClassName>(<args>)
        Foo foo = new Foo(1, 100);
        foo.incrementBar(); // good practice camel case for methods/attributes/variables. pascal case for classes
        foo.incrementBar();
    }
}