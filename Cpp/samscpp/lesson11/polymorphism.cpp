/**
 * Sam's C++ Lesson 11 - Polymorphism
 *
 */

#include <iostream>

/**
 * Fish here is an example base class.
 */
class Fish {
public:
    Fish() {
        std::cout << "Fish created" << std::endl;
    }

    /**
     * We can use the `virtual` keyword to mark a method as intended for overriding in derived classes.
     * Under the hood, the compiler creates a virtual function table (VFT), this enables runtime polymorphism.
     * As opposed to compile-time polymorphism (just simply overloading in a child class with the same signature).
     *
     * The VFT is essentially a static lookup table/array of function pointers.
     * Compile time polymorphism is faster (no runtime lookups), but runtime allows for more flexible and dynamic code
     * like dependency injection, plugin systems, etc. (more advanced than I need to know right now).
     */
    void virtual swim() {
        std::cout << "Fish is swimming" << std::endl;
    }

    /** We can use 'virtual' keyword to make the destructor virtual.*/
    virtual ~Fish() {
        std::cout << "Fish deleted" << std::endl;
    }
};

class Tuna final : public Fish {
public:
    Tuna() {
        std::cout << "Tuna created" << std::endl;
    }

    ~Tuna() override {
        std::cout << "Tuna deleted" << std::endl;
    }

    void swim() override {
        std::cout << "Tuna is swimming" << std::endl;
    }
};


int main() {
    // // Constructor order when constructing the Tuna object, the Fish constructor is called first.
    Tuna *myTuna = new Tuna();
    // output:
    //      Fish created
    //      Tuna created
    // On destructor, the class inheritance is unravelled backwords (Tuna/child class first)
    delete myTuna;
    // output:
    //      Tuna deleted
    //      Fish deleted
}
