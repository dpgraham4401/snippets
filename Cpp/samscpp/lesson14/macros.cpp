/**
 * Sam's C++ ninth edition lesson 14 - Macros and Templates
 *
 * in lesson 2, we learned about the preprocessor. It runs before the compiler.
 * in other words, we can use the preprocessor to manipulate what is compiled.
 * Macros execute text substitution, nothing crazy intelligent, just swaps the macro with
 * C++ that (hopefully) compiles.
 */

#include <iostream>

// directives start with a '#'
#define ARRAY_LENGTH 25

// creating a macro function
#define SQUARE(x) ((x) * (x))

int main() {
    int twenty_five = SQUARE(5);
    std::cout << "5 squared is " << twenty_five << std::endl;
}
