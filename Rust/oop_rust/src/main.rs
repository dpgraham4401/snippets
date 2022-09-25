// Rust is sort of an Object-Oriented Programming language

// As a statically typed language, we can define our 'object' types in a struct
struct Person {
    name: &'static str,
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
    println!("{}", jim.get_age());
    jim.increment_age();
    println!("{}", jim.get_age());
    jim.decrement_age();
    println!("{}", jim.get_age());
}
