/**
 * Sam's C++ Lesson 6 - Controlling program flow
 *
 * Again, another quick lesson just for refreshing what's available in C++
 *
 * While we're talking about swtich-case statements, this is a good place to refresh on enums.
 *
 * Enums can either be unscoped `enum Day` or scoped `enum class Day`.
 * Scoped enums are a C++11, with these, the constants are scoped to the enum (must use `Day::Sunday` instead of just `Sunday`)
 * They also do not implicitly cast to integers.
 * This avoid possible collisions and generally makes our code more readable, it's encouraged to use them.
 *
*/

#include <iostream>

/**
 * adding the `class` keyword makes the enum a scoped enum.
 */
enum class Day {
	Sunday,
	Monday,
	Tuesday,
	Wednesday,
	Thursday,
	Friday,
	Saturday
};


/**
 * If-else conditional control flow follows the classical syntax.
 * Just what you'd expect.
 */
auto simple_conditions() -> void {
	int x = 6;
	int y = 5;
	if (x > y) {
		std::cout << "X > Y" << std::endl;
	} else if (x < y) {
		std::cout << "X < Y" << std::endl;
	} else {
		std::cout << "X == Y" << std::endl;
	}
}

/**
 * C++ also has support for switch-case expressions.
 * Usual rules apply, make sure to include a break statement where appropriate.
 */
auto switch_statements() -> void {
	Day apt_day = Day::Wednesday;
	switch(apt_day) {
		case Day::Sunday:
			std::cout << "The day is Sunday" << std::endl;
			break;
		case Day::Monday:
			std::cout << "The day Monday" << std::endl;
			break;
		case Day::Tuesday:
			std::cout << "The day is Tuesday" << std::endl;
			break;
		case Day::Wednesday:
			std::cout << "The day Wednesday" << std::endl;
			break;
		case Day::Thursday:
			std::cout << "The day Thursday" << std::endl;
			break;
		case Day::Friday:
			std::cout << "The day is Friday" << std::endl;
			break;
		case Day::Saturday:
			std::cout << "The day is Saturday" << std::endl;
			break;
	}
}


/**
 * C++ has a powerful operator called the 'conditional operator'.
 * It's essentially a compact if-else syntax sugar.
 * It's also called a 'ternerary operator'.
 * Pretty cool as this is usually an operator you only see in higher level languages.
 */
auto ternerary_op() -> void {
	int x = 6;
	int y = 5;
	int max = (x > y) ? x : y; // contians the greater of the two values.
	std::cout << "max is: " << max << std::endl;
}


/**
 * while loops are also pretty standard.
 *
 * We also have the do-while loop, which is useful when
 * we want the while loop to execute at least once.
 */
auto using_while() -> void {
	std::cout << "While loops" << std::endl;
	int loops = 5;
	int i = 0;
	while (i < loops) {
		std::cout << i << std::endl;
		i++;
	}

	// Using do-while loops.
	int input;
	do {
		std::cout << "Enter a number... not 1 though, don't do it!" << std::endl;
		std::cin >> input;
		// Keep going as long as input is not equal to 1
	} while (input != 1);

}


/**
 * We can use for loops with a couple variants.
 *
 * There's the classic counter loop an the C++11 range based loops.
 * There's additional variants (e.g., c++20 range with initializers)
 *
 */
auto using_for() -> void {
	std::cout << "For loops" << std::endl;
	// Traditional counter for loop
	int loops = 5;
	// There's actually a couple variants that could be implemented here,
	// e.g., a custom incrementer `i += 2`, ommitted parts `for (; i > loops; )`
	for (auto i = 0; i < loops; i++ ) {
		std::cout << i << std::endl;
	}

	// C++11 supports range based for loops, we can use this syntax for any object that's iterable
	// that is it supports the `begin()` and `end()` method
	// Many containers/arrays support range based iteration out of the box, such as
	// vectors, arrays, list, deque, maps, sets.
	int decades[] = {10, 20, 30, 40, 50};
	for (auto decade : decades) {
		std::cout << "decade: " << decade << std::endl;
	}


	// With C++20 we can also initialize the container to iterate over within the for loop for statement
	for (int sum = 0; auto x : {1, 2, 3, 4}) {
		sum += x;
		std::cout << "Sum so far: " << sum << "\n";
	}
}

int main() {
	using_while();
}
