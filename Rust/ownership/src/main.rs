// Ownership is Rust's unique approach to memory management
// The 3 rules of ownership
// 1. Each value in Rust has an owner.
// 2. There can only be one owner at a time.
// 3. When the owner goes out of scope, the value will be dropped.

struct Person {
    name: String,
    age: i32,
}

fn main() {
    function_scope();

    // variables that do not require allocation on the heap behave similarly to other languages
    let _x = 5; // create variable and assign value of 5, passing it to a function will copy it

    // that's not the case for variables with dynamic memory allocation (e.g., not known as compiletime)
    let my_string1 = String::from("hello");
    let my_string2 = my_string1;
    // when we set my_string2 = my_string1, that info is 'moved' to my_string2, not copied my_string1 IS NOW 'INVALID'
    println!(
        "{}: <location:{:p}, value: {}>",
        stringify!(my_string2),
        &my_string2,
        my_string2
    ); // --> this is ok

    // if we'd like to make a copy, we need to use the clone method
    let my_string3 = my_string2.clone();
    println!(
        "{}: <location:{:p}, value: {}>",
        stringify!(my_string3),
        &my_string3,
        my_string3
    ); // --> this is ok

    // there's another option to 'Borrow' ownership through passing references
    let my_string4 = String::from("my string4");
    println!("in main {}", my_string4);
    borrows_var(&my_string4); // the '&' allows us to create a reference to something without taking ownership
    println!("in main {}", my_string4);

    let mut jim = Person {
        name: "jim".to_string(),
        age: 42,
    };
    borrow_struct(&jim);
    jim.say_hello();
    println!("{}'s age is {}", jim.name, jim.age);
    jim.increment_age();
    println!("{}'s age is {}", jim.name, jim.age);
    own_struct(jim);
}

fn borrow_struct(person: &Person) {
    println!("This function borrows {}", person.name);
}

fn own_struct(person: Person) {
    println!(
        "This function owns{}... in hindsight, kinda messed up",
        person.name
    );
}

impl Person {
    fn say_hello(&self) {
        // when implementing methods, we usually pass a reference to self (borrow self)
        println!("Hi, I'm {}", self.name); // however this is not mutable
    }

    fn increment_age(&mut self) {
        // if we'd like to change, we need a mutable reference
        self.age += 1; // TBH, we don't have to think that much about pointers though
    }
}

fn borrows_var(s: &String) {
    // Here's the thing, since we're borrowing s, we cannot modify it, this function doesn't own s
    println!("From borrow_var function: {}", s);
}

fn function_scope() {
    // my_string is string from the String crate in the std library(?)
    // this string resides in the scope of 'function_scope' and will be released when that scope ends
    let mut my_string = String::from("hello");
    my_string.push_str(", World!");
    println!("{}", my_string);
}
