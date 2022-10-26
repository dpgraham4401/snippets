// A package is a bundle 1 or more crates, it has aa cargo.toml
// A package can have multiple binaries in src/bin directory, but only one library

// a crate is the smallest amount of code rustc will compile (could be a single file)
// A crate can be a library or binary. src/main.rs and src/lib.rs are special files

// Rust does not implicitly map the module tree to the filesystem, we have to build it
mod my_lib; // modules are declared in the files you use them, not the file they're in
mod my_module; // this declares my_module, the compiler will look for /my_module.rs or /my_module/mod.rs

fn main() {
    let a = my_module::say_hello();
    println!("{}", a);

    let x = 2;
    let y = 6;
    let z = my_lib::multiply(x, y);
    // let b = lib::divide(x, y);
    println!("from my_lib {}: should be {}", z, {
        x * y
    });
    let mut n = my_lib::add(x, y);
    println!("{}", n);
    n = my_lib::add_again(x, y); // same result since add_again is just an alias for add
    println!("{}", n);

    let m = my_lib::divide(x, y);
    println!("from my_lib {}: should be {}", m, {
        x / y
    });
}
