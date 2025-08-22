/**
 * Sam's C++ Lesson 9: Classes and Objects
*/

#include <iostream>

/**
 * This code demonstrates the basic of classes and objects in C++.
 *
 * Class attributes/methods are private by default, unless placed in the 'public' section.
 */
class Human {
    // attributes not included in the 'public' section are private by default
    std::string name;
    std::string date_of_birth;
    std::string occupation;

public:
    /**
     * Default constructor.
     *
     * The default constructor is a what is used when an object is created without any parameters.
     * You can choose not to implement a default constructor and require that all objects
     * are instantiated with specific parameters.
    */
    Human() {
        name = "Unknown";
        date_of_birth = "0000-00-00";
        occupation = "Unknown";
    }

    /**
     * Constructors are special methods that have no return type and have the same name as the class.
     *
     * @param n name
     * @param dob date of birth in YYYY-MM-DD format
     * @param job string of their occupation
     */
    Human(const std::string &n, const std::string &dob, const std::string &job) {
        name = n;
        date_of_birth = dob;
        // Using 'this' pointer to refer to the current object's attributes
        // It's usually ommitted, but can be useful when variables names in the class's scope
        // shadow the class's attributes.
        std::string occupation = "Emporer"; // this local variable shadows the class's attribute
        this->occupation = job; // Using 'this' to refer to the class's attribute
    }

    /**
     * Constructors can be overloaded,
     * This example constructor has a default occupation.
     */
    Human(const std::string &n, const std::string &dob) {
        name = n;
        date_of_birth = dob;
        this->occupation = "Software Engineer"; // Default occupation if job is not provided
    }

    /**
     * List initialization for constructors has the same adantage as
     * list initialization with common variables. Prevent narrowing conversion,
     * makes the code a little more readable (subjective), etc.
     */
    Human(const std::string &name)
        : name(name) {
        std::cout << "Using list initialization " << std::endl;
    }

    /**
     * Class Destructors.
     *
     * Destructors are just the opposite of constructors, they're called when
     * an object is destroyed. Same syntax as constructors, except they have a
     * tilde (~) char before the method.
     *
     * Destructors are called whenever an object goes out of scope, or it's 'deleted'.
     *
     * Destructors are often a good place to make sure that heap memory is deallocated.
     *
     * If we wanted to make sure that class is only ever instantiated on the heap,
     * we could make the destructor private.
     */
    ~Human() {
        std::cout << name << " Destructed" << std::endl;
    }

    /**
     * Copy Constructor.
     *
     * When an object is copied, instance variables that cannot be copied
     * are carried over by reference (e.g. pointers).
     * This is a problem if the original object is destroyed,
     * as the copied object will still point to the original's memory.
     *
     * We can use a copy constructor to create a new object
     * that, if implemented correctly, can avoid this issue.
     */
    Human(const Human &other_human)
        : name(other_human.name), date_of_birth(other_human.date_of_birth), occupation(other_human.occupation) {
        // We don't really have anything in this class that need copying over
        // but if we had pointers or dynamic memory, we would need to
        // allocate new memory and copy the data over to avoid dangling pointers.
    }

    void introduce_self() {
        std::cout << "I'm " << this->name << ", a " << occupation << ".\n";
    }

    int get_age() {
        try {
            int birth_year = std::stoi(date_of_birth.substr(0, 4));
            return 2020 - birth_year;
        } catch (const std::exception &e) {
            std::cerr << "Error parsing date of birth: " << e.what() << '\n';
            return -1;
        }
    }

    std::string get_name() {
        return name;
    }
};

int main() {
    auto bob = Human("Bob", "1990-05-15");
    bob.introduce_self();
    int age = bob.get_age();
    std::cout << "I am " << age << " years old.\n";

    auto john = Human("john Jacob Jingle Heimerschmit");
    std::cout << "I'm " << john.get_name() << "\n";
}
