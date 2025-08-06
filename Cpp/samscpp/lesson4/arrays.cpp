/**
 * Lesson 4: Strings and arrays
 */

#include <iostream>

template <size_t N, typename T>
auto display_array(T (&arr)[N]) {
    for (const auto elem : arr) {
        std::cout << elem << ", ";
    }
    std::cout << std::endl;
}

// 2D array
template <size_t N, size_t M, typename T>
void display_array(T (&arr)[N][M]) {
    for (size_t i = 0; i < N; ++i) {
        display_array(arr[i]); // call 1D version for each row
    }
}

/**
 * C++ arrays are static, they can't change in size or element type.
 * We can init it partially, add
 */
auto static_arrays() {
    // <element_type> <array_name>[<num_elem>] = { <optional_init_values> }
    float temps[5] = {100.0, 99.5, 95.2, 92.1}; // partially init, last value will be default ('0.0')
    display_array(temps);

    // unless we make is constant, we welcome to change elements (even though they're length/type is static)
    temps[3] = 65.3;
    display_array(temps);

    // To get the length of an array, we get the number of bytes, divided by the number of bytes in 1 element.
    int length = sizeof(temps) / sizeof(temps[0]);
    length = std::size(temps); // Or just use the 'std::size' function.
    temps[length - 1] = 55.7;
    display_array(temps);
}

/**
 * Arrays can be made up of more arrays
 * C++ actually stores the multidimensional array in the same way as a 1d array.
 * C++ just maps the 1D memory array to it's x-D representation.
 */
auto multidimensional_arrays() {
    // An array with 3 rows, and 2 columns
    float data[3][2] = {{1.2, 3.3}, {2.5, 5.2}, {8.5, 7.4}};
    display_array(data);

}

int main() {
    multidimensional_arrays();
}