/**
 * Sams's C++ - Lesson 15: An intro to the Standard Template Library (STL).
 *
 * The STL is a set of template classes and functions that supply a programmer with:
 * - containers for storing data
 * - iterator for accessing stored data
 * - Algorithms that comprise utility functions that work on the containers with iterators.
 *
 * Std sequential containers:
 * These are generally characterized by fast 'insertion' times but slow 'find' times.
 * Think 'lists/arrays', instead of 'dicts/hashmaps'
 *     - std::vector --> equivalent to the 'array' of most languages.
 *     - std::deque  --> A double ended style stack that allows pushing/popping from both ends.
 *     - std::list   --> Operates like a doubly linked list.
 *     - std::forward_list --> like list, but singly linked
 *
 * Associative containers
 * These take a little longer to insert, but finding can be much faster
 * The common ones include, but there are many variants.
 *     - std::set   --> stores unique values, sorted in insertion order
 *     - std::map   --> stores key/value pairs
 *
 * Container adaptors
 * variants fo sequential and associative containers with limited
 * functionality and are intended to fulfil a particular purpose.
 *     - std::stack  --> stores in LIFO order
 *     - std::queue  --> stores in FIFO order
 *
 * STL algorithms
 * The STL also includes the following template functions, often used
 * with the STL containers.
 *     - std::find
 *     - std::reverse
 *     - std::transform
*/

// File: lesson15/stl_example.cpp
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

int main() {
    // Using std::vector
    std::vector<int> numbers = {5, 2, 9, 1, 5, 6};

    // Sort the vector
    std::ranges::sort(numbers);

    // Print sorted numbers using std::for_each and a lambda
    std::cout << "Sorted numbers: ";
    std::for_each(numbers.begin(), numbers.end(), [](int n) {
        std::cout << n << " ";
    });
    std::cout << std::endl;

    // Find a value
    auto it = std::find(numbers.begin(), numbers.end(), 5);
    if (it != numbers.end()) {
        std::cout << "Found the value '5' in vector." << std::endl;
    }

    // Using std::set (stores unique, sorted values)
    std::set<int> unique_numbers(numbers.begin(), numbers.end());
    std::cout << "Unique numbers: ";
    for (int n: unique_numbers) {
        std::cout << n << " ";
    }
    std::cout << std::endl;

    return 0;
}
