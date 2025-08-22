/**
 * Sam's  C++ lesson 11 - Abstract Base Classes (ABC)
 *
 * C++ does not have a built-in concept of interfaces like some other languages (e.g., Java, C#).
 * But we can make use of Abstract Base Classes (ABC) to achieve similar functionality.
 * The big disadvantage of this obviously being that any class that we want to fulfil that 'interface'
 * needs to inherit from that ABC.
 */

#include <iostream>


template<typename T>
/**
 * Our abstract base class (ABC) here is Fish (again, like our interface).
 * These are a great way to make sure that any derived class implements the required methods.
 */
class Fish {
protected:
    ~Fish() = default;

public:
    void virtual swim() = 0; // Pure virtual function, makes this class abstract
    void virtual eat(std::string item) = 0; // Pure virtual function
    std::vector<T> virtual get_stomach_contents() = 0; // Pure virtual function
};

/**
 * Tuna is a concrete class that inherits from the Fish ABC and implements its pure virtual functions.
 * We're also marking it 'final' to prevent further inheritance.
 */
class Tuna final : public Fish<std::string> {
    std::vector<std::string> stomach; // Tuna's stomach to store eaten items
public:
    void swim() override {
        std::cout << "Tuna is swimming" << std::endl;
    }

    void eat(std::string item) override {
        std::cout << "Tuna is eating " << item << std::endl;
        stomach.push_back(item);
    }

    std::vector<std::string> get_stomach_contents() override {
        return stomach;
    }
};

template<typename F>
void do_fishy_things(Fish<F> *fish) {
    fish->swim();
    fish->eat("plankton");
    fish->eat("algea");
    std::cout << "Stomach contents:" << std::endl;
    for (const auto &item: fish->get_stomach_contents()) {
        std::cout << "\t" << item << std::endl;
    }
}

int main() {
    // Creating an object that fulfils the Fish 'interface'
    Tuna *steve = new Tuna();
    do_fishy_things(steve);
    delete steve;
}

