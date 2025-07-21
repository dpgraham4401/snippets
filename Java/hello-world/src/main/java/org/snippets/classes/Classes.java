// This snippet looks at java classes, constructors, properties, and methods
package org.snippets.classes;

import java.util.Random;

class MyClass {

    public int c; // public access modifier, an instance variable, can be accessed from anywhere
    protected int d; // protected access modifier,
    int a; // default access modifier, an instance variable
    private int b; // private access modifier, an instance variable
    // an instance variable, can be accessed from the same package or by subclasses

    // Constructors share the same name as the class
    // A class can have multiple constructors, as long as they have different parameters (overloaded)
    public MyClass(int a, int b, int c, int d) {
        this.a = a;
        this.b = b;
        this.c = c;
        this.d = d;
    }

    // generally speaking, it's good practice to use Factory Methods instead of
    // constructor overloading for constructors
    // https://stackoverflow.com/questions/997482/does-java-support-default-parameter-values
    public MyClass(int a, int b, int c) {
        this.a = a;
        this.b = b;
        this.c = c;
        this.d = 0; // default value
    }


    // static method that returns an integer, can be called without instantiating
    public static int getNumber() {
        return new Random().nextInt();
    }

    // Getters and setters should be used to access and modify private instance variables
    public int getB() {
        return b; // this.b is also valid, but not necessary unless it's shadowed
    }

    public void setB(int b) {
        this.b = b;
    }

}

public class Classes {

    public static void main(String[] args) {
        System.out.println(MyClass.getNumber());
        MyClass myClass = new MyClass(1, 2, 3, 4);
        System.out.printf("this.a: %d\n", myClass.a); // -> only accessible because it's in the same package
        // System.out.println(myClass.b); -> this will not work because it's private
        System.out.printf("this.b: %d\n", myClass.getB());
        System.out.printf("this.c: %d\n", myClass.c);
        System.out.printf("this.d: %d\n", myClass.d);
    }


}
