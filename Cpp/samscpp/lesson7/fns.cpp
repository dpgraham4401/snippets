/**
 * Sam's C++, 9th edition, lesson 7 - Functions
 *
 * More of a refresher than anything, but it's good to take the time to learn what's new in C++.
 */

#include <iostream>
#include <string>
#include <memory>


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
Foo multiple_input_output(std::string callout, Foo foo) {
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
auto sum(int x, int y) -> int {
	return x + y;
}

auto sum(int x, int y, int z) -> int {
	return x + y + z;
}



/**
 * If we have a large (memory) object, it's inefficient to try and 
 * copy a huge chunk of memory, so instead we pass a reference.
 *
 * Use the `&` operator to indicate a parameter expects a reference.
 */
int passing_by_reference(Foo& foo) {
	int duh_num = foo.num;
	std::cout << "pass by ref: " << duh_num << std::endl;
	return duh_num;
}

int main() {
	// double radius = 4.0;
	// auto area = get_circle_area(radius); // note, we're not supplying pi... but we could add more precision.
	// std::cout << area << std::endl;

	// Foo my_foo = Foo{"bar", 1};
	// auto new_foo = multiple_input_output("yaahooo!", my_foo); // note we're not passing by ref
	// std::cout << new_foo.num << std::endl;

	// // Function overloading
	// int x = 1, y = 2, z = 3;
	// int sum1 = sum(x, y);
	// int sum2 = sum(x, y, z);
	// std::cout << "sum1: " << sum1 << " sum2: " << sum2 << std::endl;
	
	// Passing by reference
	std::unique_ptr<Foo> my_foo = std::make_unique<Foo>(Foo{"foo", 3});
	int result = passing_by_reference(*my_foo);
	std::cout << "result: " << result << std::endl;
}
