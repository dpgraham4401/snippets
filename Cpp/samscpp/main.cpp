/**
 * Parts of a program
*/

// Preprocessor directives
// All start with a hash (#), they run before the compiler.
#include <iostream> // often called 'hash include', 'sharp include', or 'pound include'
// we use quotes ("") for local files and angle brackets (<>) for standard library files
// A large number of includes can slow down compilation, however with C++20 modules, this is less of an issue.

// By convention, main returns an int, and 0 for success, -1 for error, used by OS.
int main() {
    // Can declare that we're using a namespace in a function or globally in a file.
    using namespace std;
    int nLoops;
    cout << "Enter number of loops: ";
    cin >> nLoops;
    if (cin.fail()) {
        cout << "Invalid input." << endl;
        return EXIT_FAILURE; // or -1, same-same
    }
    for (int i = 0; i < nLoops; ++i) {
        // "standard see-out and "standard see-in"
        cout << "i = " << i << endl;
    }
    return EXIT_SUCCESS; // or 0, same-same
}
