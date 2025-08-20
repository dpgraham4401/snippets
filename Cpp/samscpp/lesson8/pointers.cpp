/**
 * Sams's C++ - Lesson 8: Pointers and References
 *
 * Something awesome about C++ is its ability to write high-level code or low-level code close to the hardware.
 * A pointer is simply a variable that holds the address of another variable in memory.
 *
*/

#include <iostream>

/**
 * The 'Reference' and 'Dereference' operators.
 *
 * Basically, use '&' (reference) to get the address of a variable,
 * use '*' (dereference) to get the value at that address.
 *
 * We use the '*' operator to declare a pointer variable, which has always seemed backwards to me.
 */
void basic_pointers() {
    int x = 1;
    // If 'X' is a variable, then '&X' gives the location of that variable in memory
    std::cout << "X: " << x << std::endl;
    // The `&` is called the "address of" operator, or the "reference operator".
    std::cout << "X location: " << &x << std::endl;

    // We use the '*' operator to declare a pointer variable
    int *pX = &x; // pX is a pointer to an integer,
    // To get the value stored at the address pointed to by pX, we use the '*' operator again
    std::cout << "Value at pX: " << *pX << std::endl;
    // The '*' (dereference) operator is also called the 'indirection' operator.
}

/**
 * Dynamically allocating memory with 'new' and 'delete'.
 *
 * in C++, we can allocate memory with the 'new' keyword.
 * This is allocated from the 'free store', which an abstraction in the form of a pool of memory.
 */
void new_and_delete() {
    // 'new' can be used to allocate memory.
    // A memory allocation is not guaranteed, this can throw an exception.
    int *x_pointer = new int{2}; // new returns a pointer
    std::cout << *x_pointer << std::endl;
    *x_pointer = 1;
    std::cout << *x_pointer << std::endl;
    // We have to use 'delete' with 'new' or our memory will leak (will never be released).
    // This can get harry, if the distance between our allocation and deallocation increases.
    delete x_pointer;
}

/**
 * Pointers can be incremented and decremented.
 *
 * When a pointer is incremented (++) or decremented (--), the compiler interprets
 * that as needing to move to the next memory location, not the value.
 */
void inc_and_dec_pointers() {
    int num_entries = 0;
    std::cout << "Enter number of entries: " << std::endl;
    std::cin >> num_entries;

    int *nums = new int[num_entries];

    for (int i = 0; i < num_entries; ++i) {
        std::cout << "Enter number # " << i + 1 << ": ";
        std::cin >> *(nums + i);
    }
    for (int i = 0; i < num_entries; ++i) {
        std::cout << nums[i] << " ";
    }
    std::cout << std::endl;
    delete[] nums;
}

struct Person {
    std::string name;
    int age;
};

/**
 * Using a pointer to pass an object by reference is usually more efficient
 * than the alternative.
 *
 * We can also make pointers `const`, or the value of the pointer is `const` as well (or both).
 */
void passing_data_with_pointers(const Person *person) {
    // Accessing member of a struct through a pointer
    // uses the '->' (arrow) operator, which is shorthand for dereferencing the pointer and accessing the member.
    std::cout << "Name: " << person->name << std::endl;
    // This is equivalent to:
    std::cout << "Age: " << (*person).age << std::endl;
}

/**
 * A reference is an alias for a variable.
 * It is not a pointer, but it can be used in a similar way.
 * References are often used to avoid copying large objects into functions.
 *
 * Using const on a reference means that the reference's value cannot be changed,
 */
void was_ist_ein_reference(int &age, const std::string &name) {
    int &age_ref = age; // age_ref is a reference to age
    std::cout << "Original Age: " << age_ref << std::endl;
    age_ref = 51; // changing the reference changes the original variable
    std::cout << "Age changed thru ref: " << age << std::endl;
    // if we don't include the '&' in the declaration, we create a copy of the variable
    int age_copy = age; // age_copy is a copy of age
    age_copy = age_copy + 1; // changing the copy does not change the original variable
    std::cout << "Age copy: " << age_copy << std::endl;
    std::cout << "Age: " << age << std::endl;

    // name cannot be changed
    // name = "John"; // this will not compile, since name is a const reference
}

int main() {
    int age = 45;
    const std::string name = "Sam";
    was_ist_ein_reference(age, name);
}
