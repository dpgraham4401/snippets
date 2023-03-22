package org.example;
// Java packages often follow a reverse domain

// The 'Main' class (note capitalization) has special significance
public class Main {
    // The main method of the Main class is also special
    public static void main(String[] args) {
        // we can call this method without instantiating b/c it's a static method
        FooBar.hello();
        // To instantiate a new object: <ClassName> <VarName> = new <ClassName>()
        FooBar foo = new FooBar(1);
        foo.booBoo();
    }
}

// I can declare another class in the same file, but another public class should be in another file
class FooBar {
    int boo;

    public FooBar(int boo) {
        this.boo = boo;
    }

    // methods need to be explicitly declared as 'public', or they're private
    // 'static' indicates that method belong to the class, not the instance
    // 'void' indicates the return type
    public static void hello() {
        System.out.println("Hello world!");
    }

    public void booBoo() {
        System.out.printf("boo is %d", this.boo);
    }
}