/**
 * Sam's C++, 9th edition, lesson 7 - Functions
 *
 * More of a refresher than anything, but it's good to take the time to learn what's new in C++.
 */

#include <iostream>


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
	string name;
	int num;
};

/**
 * I've been spending a lot of my time with dynamic languages, with static langs
 * if you need to pass in lots of values, it may make sense to group related parameters
 * into a data struct
 */
void multiple_input_output(string callout, Foo foo) {

}

int main() {
	// double radius = 4.0;
	// auto area = get_circle_area(radius); // note, we're not supplying pi... but we could add more precision.
	// std::cout << area << std::endl;
}
