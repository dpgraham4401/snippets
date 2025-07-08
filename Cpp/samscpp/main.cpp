/**
 * Chapter 3: Using variables, declaring constants.
*/

#include <iostream>

int main() {
    // Declare a variable
    // <variableType> <variableName>
    int a;

    // Declaring and initializing
    // <variableType> <variableName> = <value>
    // It's good practice to initialize variables so we're not working with garbage values.
    int b = 5;

    int x = -1, y = -1;

    std::cout << "Enter a positive integer for x: ";
    std::cin >> x;
    std::cout << "Enter a positive integer for y: ";
    std::cin >> y;
    const int product = x * y;
    std::cout << "The product of " << x << " and " << y << " is: " << product << std::endl;
}
