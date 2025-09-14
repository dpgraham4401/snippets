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

/**
 * multi parameter templates, and defaults
 *
 * we can declare type templates with more than 1 parameter.
 * We can also add default parameter types, in the below, T2 will be an int
 * unless specified otherwise.
 */
template<typename T1, typename T2=int>
class Foo {
    T1 foo;
    T2 bar;

public:
    Foo(T1 t1, T2 t2) {
        foo = t1;
        bar = t2;
    }
};

// Here, we only had to specify 1 type, and allow T2 to use the default type of int
auto foo = Foo<std::string>("foo", 1);

int main() {
    int twenty_five = SQUARE(5);
    std::cout << "5 squared is " << twenty_five << std::endl;
}
