/**
 * Sam's C++, 9th edition, lesson 7 - Functions
 *
 * More of a refresher than anything, but it's good to take the time to learn what's new in C++.
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <memory>
#include <vector>


/**
 * We can supply default values, they just need to be at the end of the function prototype.
 */
double get_circle_area(double radius, double pi = 3.14) {
	return pi * radius * radius;
}


/**
 * An simple, example structure
 */
struct Foo {
	std::string name;
	int num;
};

/**
 * I've been spending a lot of my time with dynamic languages, with static langs
 * if you need to pass in lots of values, it may make sense to group related parameters
 * into a data struct (also consider where it needs to be passed by reference).
 */
Foo multiple_input_output(const std::string &callout, const Foo &foo) {
	std::cout << callout << std::endl;
	// Unlike many languages, the `new` keyword is not used to just create new objects.
	// `new` in C++ is used for allocating memory on the heap.
	Foo new_foo = Foo{foo.name, foo.num + 1};
	return new_foo;
}

/**
 * Overloading functions.
 *
 * Since we're not using a dynamic lang, if we want to create a function that 
 * accepts differenet sets of parameters, we need to write two versions of that function.
 * This is different than using generics, since that's the same number of parameters but
 * a differenet type for each parameter. 
 *
 * This is a poor example, but focus on the overloading fn part.
 */
auto sum(const int x, const int y) -> int {
	return x + y;
}

auto sum(const int x, const int y, const int z) -> int {
	return x + y + z;
}


/**
 * If we have a large (memory) object, it's inefficient to try and 
 * copy a huge chunk of memory, so instead we pass a reference.
 *
 * Use the `&` operator to indicate a parameter expects a reference.
 */
int passing_by_reference(const Foo &foo) {
	const int duh_num = foo.num;
	std::cout << "pass by ref: " << duh_num << std::endl;
	return duh_num;
}

/**
 * Inline Functions.
 *
 * C++ has the concept of `inline` functions. Inline functions are an optimization
 * that reduces the overhead of a function call (adding a fn call to the stack).
 * C++ does that at compile time by replacing the inline function call with the contents
 * of the function where it is called.
 *
 * They're best used sparingly, modern C++ have various performance optimizations that may outweigh
 * the complexity and compiling for memory restricted runtimes may even reject these (or so I read).
 *
 * These are not the same thing as lambda functions, a more common concept.
 */
float double_value(const float val) {
	return val * val;
}


/**
 * Lambda functions.
 *
 * Also called "Lambda Expressions." Lambda functions are commonly used by the Standard Template Library (STL)
 * such as within a `sort` function.
 */
void simple_lambda_usage() {
	std::vector<int> nums;
	nums.push_back(120);
	nums.push_back(-1);
	nums.push_back(250);
	nums.push_back(500);
	nums.push_back(375);

	// Here's our first usage, using the for_each function
	std::cout << "Unsorted vector" << std::endl;
	std::for_each(nums.begin(), nums.end(), [](int element) { std::cout << element << " "; });

	// Here, we're using a lambda fn for the sort std lib algorithm
	std::ranges::sort(nums, [](int num1, int num2) { return (num2 < num1); });

	std::cout << "Sorted vector" << std::endl;
	std::ranges::for_each(nums, [](int element) { std::cout << element << " "; });
}

int main() {
	// // Basic functions and default parameters
	// double radius = 4.0;
	// auto area = get_circle_area(radius); // note, we're not supplying pi... but we could add more precision.
	// std::cout << area << std::endl;

	// // Using structs to group related parameters
	// Foo my_foo = Foo{"bar", 1};
	// auto new_foo = multiple_input_output("yaahooo!", my_foo); // note we're not passing by ref
	// std::cout << new_foo.num << std::endl;

	// // Function overloading
	// int x = 1, y = 2, z = 3;
	// int sum1 = sum(x, y);
	// int sum2 = sum(x, y, z);
	// std::cout << "sum1: " << sum1 << " sum2: " << sum2 << std::endl;

	// // Passing by reference
	// std::unique_ptr<Foo> my_foo = std::make_unique<Foo>(Foo{"foo", 3});
	// int result = passing_by_reference(*my_foo);
	// std::cout << "result: " << result << std::endl;

	// Using Lambda functions
	simple_lambda_usage();
}
