package org.foo;
// Java packages often follow a reverse domain

// we declare public classes in their own package
public class Foo {
    int bar; // an instance of the class Foo has an attribute 'bar'. It can only be accessed within the package
    // private int blu; private attributes are different from the default
    public int bla; // an instance has public attribute 'bla'
    public static int ble; // A public attribute of the class

    public Foo(int bar, int bla) {
        this.bar = bar;
        this.bla = bla;
    }

    /**
     * We can document our functions using document comments like so
     *
     * @param bar a boolean that will affect what is said
     */
    public static void sayFoo(boolean bar) {
        String foo = "foo";
        if (!bar) {
            System.out.println(foo);
        } else {
            System.out.println(foo.concat("bar"));
        }
    }

    /**
     * increment bar and print to results
     */
    public void incrementBar() {
        System.out.printf("bar before:\t%d\n", this.bar);
        ++this.bar;
        System.out.printf("bar after:\t%d\n", this.bar);
    }
}