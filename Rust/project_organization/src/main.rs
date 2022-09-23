// A package is a bundle of crates, contains a cargo.toml
// A package can have multiple binaries in src/bin directory, but only one library

// a crate is the smallest amount of code rustc will compile (could be as small as a single file
// A crate can be a library or binary
// src/main.rs and src/lib.rs are special files that indicates to cargo what kind of crate it is


mod my_module; // option 1 for importing a module, use the mod keyword

fn main() {
    let x = 2;
    let y = 7;
    let z = my_module::add(x, y); // you can access my_module functions via '::' syntax (wierd)
    println!("from my_module::add {}", z);
}
