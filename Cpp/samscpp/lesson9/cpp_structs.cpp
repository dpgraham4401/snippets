/**
 * Sam's C++ Lesson 9 - Structs.
 *
 * The Struct keyword is kind of a holdover from C.
 * It's largely treated the same as a class in C++, with some noteable exceptions:
 * 1. Members of a struct are public by default, while members of a class are private by default.
 * 2. Structs are typically used for plain data structures, while classes
 *    are used for more complex objects with methods and encapsulation.
 */

#include <iostream>
#include <string>
#include <utility>

/**
 * This is a simple struct definition.
 * It's just like a C struct. Simple does it.
 */
struct Person {
    std::string name;
    int age;
    std::string occupation;
};

/**
 * In C++, structs can also have members declared private, we can have
 * member functions, constructors, destructors, and even inheritance.
 * It's a bit weird, I'm kind of of-the-mind that structs should be simple data structures.
 */
struct Animal {
    std::string species;
    int age;
    std::string habitat;

    Animal(std::string spec, int a, std::string hab)
        : species(std::move(spec)), age(a), habitat(std::move(hab)) {
    }

    void speak() const {
        std::cout << "Bark! I am a " << species << "!" << std::endl;
    }
};

int main() {
    // // If we want to construct a simple struct, it's just like a C struct.
    // Person bob = {"Bob", 30, "Software Engineer"};
    // std::cout << bob.name << std::endl;

    // More complex structs with OOP like features
    Animal dog = {"Dog", 5, "Domestic"};
    std::cout << "Species: " << dog.species << ", Age: " << dog.age << std::endl;
    dog.speak();
}
