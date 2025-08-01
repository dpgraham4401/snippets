/**
 * Chapter 3: Using variables, declaring constants.
*/

#include <iostream>

// Global constants
const int MAX_SIZE = 100;
const int MIN_SIZE = 1;
// As with all other langs, avoid global variables unless necessary.

int main() {
    // Declare a variable
    // <variableType> <variableName>
    // By convention, variables use camelCase names. snake_case is ok, just depends on the team's style guide.
    int firstNumber;

    // Declaring and initializing
    // <variableType> <variableName> = <value>
    // It's good practice to initialize variables so we're not working with garbage values.
    int secondNumber = 5;

    int x = -1, y = -1;

    std::cout << "Enter a positive integer for x: ";
    std::cin >> x;
    std::cout << "Enter a positive integer for y: ";
    std::cin >> y;
    if (x < MIN_SIZE || x > MAX_SIZE || y < MIN_SIZE || y > MAX_SIZE) {
        std::cout << "Please enter values between " << MIN_SIZE << " and " << MAX_SIZE << "." << std::endl;
        return EXIT_FAILURE; // Exit the program with an error code
    }
    const int product = x * y;
    std::cout << "The product of " << x << " and " << y << " is: " << product << std::endl;

    // Common variable types
    bool isValid = true; // true of false
    char grade = 'A'; // single character, enclosed in single quotes
    unsigned short int foo = 65'535; // 0 to can use single quotes for readability, but not required
    short int shortInt = -32'768; // to positive equivalent
    long int longInt = -12'356'789;
    long long longLongInt = -9'223'372'036'854'775'808; // 64-bit integer, can be used for large numbers
    int myInt = 42; // whether it's 16 or 32 bits depends on the system, but it's usually 32 bits on modern systems

    return EXIT_SUCCESS;
}
