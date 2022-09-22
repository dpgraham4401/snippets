// Ownership is Rust's unique approach to memory management
// other languages either...
// 1. garbage collector --> Runtime checking variables via some process (e.g., Python, Go)
// 2. Manual Memory Mngt. --> like C, memory is managed by developer (e.g., C, c++)

// The 3 rules of ownership
// 1.Each value in Rust has an owner.
// 2. There can only be one owner at a time.
// 3. When the owner goes out of scope, the value will be dropped.

fn main() {
    function_scope();

    // Moves
    // variables that do not require allocation on the heap behave similarly to other languages
    let x = 5; // create variable and assign value of 5
    let y = x; // create a new variable, y, and assign the value of x

    // that's not the case for variables with dynamic memory allocation (e.g., not known as compiletime)
    let my_string1 = String::from("hello");
    // This returns a String, which is actually 3 parts stored on the stack
    // 1. a pointer to heap 2. a length, 3. capacity
    let my_string2 = my_string1;
    // when we set my_string2 = my_string1, that info is 'moved' to my_string2, not copied
    // my_string1 IS NOW BASICALLY INVALID
    // println!("{}", my_string1); // --> throws an error
    println!("{}: <location:{:p}, value: {}>", stringify!(my_string2), &my_string2, my_string2); // --> this is ok

    // Cloning
    // if we'd like to make a copy, we need to use the clone method
    let my_string3 = my_string2.clone();
    println!("{}: <location:{:p}, value: {}>", stringify!(my_string3), &my_string3, my_string3); // --> this is ok


    // Ownership w/ functions
    // passing arguments will either 'move' or 'copy', if you'd like to clone, you need to do that yourself
    takes_ownership(my_string3);
    // println!("{}", my_string3); // --> throws an error since 'takes_ownership' took
    // this variable and released it when the scope finished

    // References
    // there's another option to 'Borrow' ownership through passing references
    let my_string4 = String::from("my string4");
    println!("in main {}", my_string4);
    borrows_var(&my_string4);
    println!("in main {}", my_string4);
    // the & allows us to create a reference to something without taking ownership

    let mut my_string5 = String::from("a lonely string");
    // we can have mutable references, see 'mut_borrow' function
    println!("\n");
    println!("in main again: {}", my_string5); // --> prints the orig string
    mut_borrow(&mut my_string5); // --> mutates and prints new string via reference
    println!("in main again: {}", my_string5); // --> prints the mutated string again
}

fn mut_borrow( s: &mut String) {
    s.push_str(", plus this additional string");
    println!("From mut_borrow function: {}", s);
}

fn borrows_var(s: &String) {
    // Here's the thing, since we're borrowing s, we cannot modify it, this function doesn't own s
    println!("From borrow_var function: {}", s);
}

// this function will take ownership of the string passed in
fn takes_ownership(my_string: String) {
    println!("{}", my_string);
}

fn function_scope() {
    // my_string is string from the String crate in the std library(?)
    // this string resides in the scope of 'function_scope' and will be released when that scope ends
    let mut my_string = String::from("hello");
    my_string.push_str(", World!");
    println!("{}", my_string);
}
