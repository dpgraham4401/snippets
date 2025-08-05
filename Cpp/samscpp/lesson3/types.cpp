/**
 * Lesson 3: variables, constants, and types
*/

#include <compare>
#include <iostream>
#include <vector>

// Global constants
const int MAX_SIZE = 100;
const int MIN_SIZE = 1;
// As with all other langs, avoid global variables unless necessary.


/**
 * We can use the sizeof operator to get the number of bytes in a variable
 * @param x
 * @return int
 */
auto get_size_of(int x) -> int {
    return sizeof(x);
}

/**
 * Using list/uniform initialization
 * We can accidentally narrow a type at initialization and round part of our data.
 * C++ version 11 allows us to init with {}, it's the recommended method of init variables.
 */
void uniform_init() {
    float temperature = 79.23;
    int temp = temperature; // decimal values will be lost, c++ will warn but not error
    std::cout << "rounded temp " << temp;
    // int error_temp{temperature}; // will not compile
    float list_temp{temperature}; // OK
}

template <typename T>

/**
 * The C++ compiler is smart and can save us some time by inferring types with 'auto'
 *
 * Right off the bat, we can use 'auto', along with the trailing return type.
 * The trailing return type (-> type) has the following advantages:
 * 1. readability. It's nice, like a python type hint
 * 2. Allows us to use a 'template' in the return type
 */
auto type_inference_with_auto(const T& x, const T& y) -> T {
    auto my_int = 1; // C++ figures this is an int
    std::vector<float> temps {97.32, 85.38, 99.55}; // we can use uniform init to create a vector as well
    // auto can make range iteration over a iterable easier
    for (auto temp : temps) {
        std::cout << "temp: " << temp <<std::endl;
    }
    return x + y;


}

void variable_types() {
    // Declare a variable
    // <variableType> <variableName>
    // By convention, variables use camelCase names. snake_case is ok, just depends on the team's style guide.
    int firstNumber;

    // Declaring and initializing
    // <variableType> <variableName> = <value>
    // It's good practice to initialize variables so we're not working with garbage values.
    int second_number = 5;

    int x = -1;
    int y = -1;

    std::cout << "Enter a positive integer for x: ";
    std::cin >> x;
    std::cout << "Enter a positive integer for y: ";
    std::cin >> y;
    if (x < MIN_SIZE || x > MAX_SIZE || y < MIN_SIZE || y > MAX_SIZE) {
        std::cout << "Please enter values between " << MIN_SIZE << " and " << MAX_SIZE << "." << std::endl;
    }
    const int product = x * y;
    std::cout << "The product of " << x << " and " << y << " is: " << product << std::endl;

    // Common variable types
    bool is_valid = true; // true of false
    char grade = 'A'; // single character, enclosed in single quotes
    unsigned short int foo = 65'535; // 0 to can use single quotes for readability, but not required
    short int short_int = -32'768; // to positive equivalent
    long int long_int = -12'356'789;
    long long long_long_int = -9'223'372'036'854'775'808; // 64-bit integer, can be used for large numbers
}

auto main () -> int {
    auto the_answer = 42;
    auto the_answer_again = 42;
    auto result = type_inference_with_auto(the_answer, the_answer_again);
    std::cout << "Result: " << result << std::endl;

    return EXIT_SUCCESS;
}

