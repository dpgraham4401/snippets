// Rust is sort of an Object-Oriented Programming language

use std::fmt;

// As a statically typed language, we can define our 'object' types in a struct
#[derive(Debug)] // with this we can print the struct via println!, meant for debugging purposes
struct Person {
    name: &'static str, // we will normally use a string instead of &str
    age: i32,
}

// We can attach method to a struct
impl Person { // an 'impl block' defines the method for a struct
    // passing a reference to &self allows immutable access to struct members
    fn get_age(&self) -> i32 {
        return self.age;
    }
    fn say_hello(&self) -> &str {
        return self.name;
    }
    // passing '&mut self' means we can mutate struct members
    fn increment_age(&mut self) {
        self.age += 1;
    }
}

impl Person { // we can define multiple impl blocks for the same struct
    fn decrement_age(&mut self) {
        self.age -= 1;
    }
}

fn main() {
    let mut jim = Person { name: "jim", age: 42 };
    println!("#[derive(Debug)]: {:?}", jim); // b/c of #[derive(Debug)], we can print the struct with "{:?}"
    println!("{}", jim.get_age());
    jim.increment_age();
    println!("{}", jim.get_age());
    jim.decrement_age();
    println!("{}", jim.get_age());

    // see the trait definition on the Person class
    jim.say_hello(); // Person, explicitly, implements the Talker trait (i.e. interface), and can use say_hello
    println!("from the Talker trait: {}", jim.give_age());
    // We can implement traits from std lib,
    println!("{}", jim); // e.g., we needed to implement the fmt::Display for this to work

    talker_impl_required(jim);

}

// a blog on additional traits from the std lib that can be implemented
// https://github.com/pretzelhammer/rust-blog/blob/master/posts/tour-of-rusts-standard-library-traits.md
impl fmt::Display for Person {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "hello, im a Person struct with name {}, and age {}", self.name, self.age)
    }
    
}

// a trait is equivalent to what other languages call an 'interface'
trait Talker { // a struct in Rust can implement an interface
// (unlike go, it needs to explicitly implement the interface)
    fn say_hello(&self);
    fn give_age(&self) -> i32;
}

impl Talker for Person {
    fn say_hello(&self) {
        println!("hello, my name is {}", self.name);
    }
    fn give_age(&self) -> i32 {
        return self.age;
    }
}

// now I can create functions that require params that implement our interface
fn talker_impl_required(person: impl Talker) {
    let person_age = person.give_age();
    println!("from talker_impl_required function: {}", person_age);
}