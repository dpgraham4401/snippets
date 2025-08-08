/**
 * Sam's C++ lesson 5 - operators
 *
 * This should be a quick one.
*/

#include <iostream>

/**
 * Common mathematical operations... pretty straightforward.
*/
auto common_ops() {
 float x = 100.0;
 float y = 5.0;
 float z = 3.0;
 float result = 0.0;
 // multiplying
 result = x * y;
 std::cout << result << std::endl;
 // dividing
 std::cout << result / y << std::endl;
 // modulus
 std::cout << 5 % 3 << std::endl;
 // minus
 std::cout << y - x << std::endl;
}

/**
 * We can use the '++' and the '--' to increment and decrement and value, respectively.
 *
 * Something we need to keep in mind is postfix vs prefix.
 * We need to learn about l-values and r-values first.
 * An l-value refers to a location in memory. An r-value can be the actual content of the memory location.
 * All l-values can be r-values, but not all r-values can be l-values.
 * variables and objects are l-values.
 * An r-value is a temporary values that may not have a persistent memory address.
 */
auto inc_and_dec() {
 int x = 100;
 int y = 5;
 // The common use case is incrementing a loop counter
 for (int i = 0; i < y; i++) {
  std::cout << i << std::endl;
 }
 // Postfix vs prefix
 int post_inc = x++;
 //  The post_inc is assigned first, then x is incremented
 std::cout << "Result of postfix inc: " << post_inc << std::endl; // 100
 std::cout << "After postfix inc: " << x << std::endl; // 101

 x = 100; // reset
 int pre_inc = ++x;
 // x is incremented first, and then assigned to pre_inc
 std::cout << "Result of prefix inc: " << pre_inc << std::endl; // 101
 std::cout << "After prefix inc: " << x << std::endl; // 101
}

/**
 * C++ version 11 and greater, we have a couple equality operators
 * @return void
 */
auto comparison_ops() {
 int x = 6;
 int y = 5;
 // we have the usual '==' and '!=' operators to test equality. Nothing special here.

 // We also have the 3-way operator in C++ 2020. '<=>'
 // will be an a 'strong_ordering' either less than zero, 0, or greater than zero
 std::strong_ordering result = x <=> y;
 if (result < 0) {
  std::cout << "X is less than Y" << std::endl;
 } else if (result == 0) {
  std::cout << "X equals Y" << std::endl;
 } else {
  std::cout << "X is greater than Y" << std::endl;
 }
}

/**
 * Boolean operators, again, nothing unexpected.
 * @return
 */
auto boolean_ops() {
 bool my_truth = true;
 bool my_false = false;
 if (my_truth && true) {
  // && -> and logical operator
  std::cout << "truth and true are true" << std::endl;
 }

 if (my_false || true) {
  // || -> the or logical operator
  std::cout << "either false or true is true" << std::endl;
 }
}

// Something I'm not bothering to cover here it bitwise operators
// NOT --> ~
// AND --> &
// OR  --> |
// XOR --> ^
// Right Shift --> >>
// Left Shift --> <<
// unlike logical operators, bitwise operators don't return true and false.
// these operate at the bit level.

// Another thing I'm leaving untouched, because I haven't really needed to bother with
// bitwise operator precedent

int main() {
 boolean_ops();
}
