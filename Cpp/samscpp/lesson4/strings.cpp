/**
 * Sam's CPP, 9th edition Lesson 4 - strings.
 *
 * C++ makes it easy to work with strings, relative to its C counterpart.
 * To use C++ strings, we can include the <string> header.
*/

#include <cstring>
#include <iostream>
#include <string>

/**
 * A C-style string is a special case of an array of chars.
 *
 * Using c-style strings is fraught with danger,
 * generally we want to avoid this dealing with null characters,
 * static char array sizes, buffer overflows, etc.
 *
 * We generally just want to use std::string instead.
*/
auto c_style_strings() -> void {
    // This is essentially a C-style string,
    std::cout << "Hello World" << std::endl; // "Hello World"
    // it's equivalent to
    constexpr char hello_world[] = {'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '\0'};
    // The cstring header includes strlen method
    auto str_length = strlen(hello_world);
    std::cout << "Outputting: " << hello_world << ", a string of length: " << str_length << std::endl; // "hello world"
    // The '\0' is a null char which tell that compiler that the string has ended.
    constexpr char foo_string[] = {'f', 'o', 'o'};
    // See what happens when we don't include the ending null char, will spit out more character
    // in this case, it seems to show "Hello World" again until it reaches a null char
    std::cout << foo_string << std::endl; // "foohello world"
}

/**
 * C++ standard string are generally more efficient and safer way to deal with user input and dynamic strings.
 * It's also wicked easy.
 */
auto using_std_string() -> void {
    // simplest way to create a string
    std::string greeting = "Hello there!";

    // We can type a string of any length into this puppy, no problem, C++'s got us.
    std::cout << "Enter a string, any string: ";
    std::string first_line;
    std::cin >> first_line;
    std::cout << first_line << std::endl;
}

int main() {
    using_std_string();
}
