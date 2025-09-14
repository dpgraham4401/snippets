/**
 * Sam's C++ ninth edition lesson 14 - Macros and Templates
 *
 * in lesson 2, we learned about the preprocessor. It runs before the compiler.
 * in other words, we can use the preprocessor to manipulate what is compiled.
 * Macros execute text substitution, nothing crazy intelligent, just swaps the macro with
 * C++ that (hopefully) compiles.
 *
 *  Advantages:
 *  - Macros allow us to reuse utility fns, regardless of the types.
 *
 *  disadvantages:
 *  - Macros are not type safe, they just do text substitution.
 *  - Debugging macros can be difficult, as the error messages may not point to the
 *  - They can make things more complex to understand if they're overused.
 *
 *  We should generally avoid using macros when possible.
 *
 *  Templates:
 *  Templates are a more modern and type-safe way to create generic code.
 */

#include <iostream>

// directives start with a '#'
#define ARRAY_LENGTH 25

// creating a macro function
#define SQUARE(x) ((x) * (x))

// Templates are defined using the 'template' keyword
// template <parameter list>

/**
 * We can also use a C++20 feature called a "concept"
 * https://en.cppreference.com/w/cpp/language/constraints.html
 */
template<typename Numeric>
    requires std::is_arithmetic_v<Numeric> // this is a C++20 feature called a "concept"
Numeric square(const Numeric val) {
    return val * val;
}

int main() {
    int twenty_five = SQUARE(5);
    std::cout << "5 squared is " << twenty_five << std::endl;
}
