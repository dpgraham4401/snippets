// Rust has a strange syntax that feels like a cross between c++ and JavaScript, so beware

// 'main' is always the entrypoint for binary applications.
fn main() {
    // variables declared with let are immutable by default
    let x = 10;
    println!("x starts out as {}", x);
    // x = x + 1 // this will not even compile in Rust you can change that with 'mut' keyword
    let mut y = 41;
    y = y + 1;
    println!("{}", y);
    let x = "string"; // things can be overshadowed
    println!("x is now {}", x);

    // TYPES
    // rust is a statically typed language and has an overkill of types
    // bits     signed  unsigned            // floats, all floats are unsigned
    // 8-bit	i8  	u8                  // 32-bit	___ 	f32 // single precision
    // 16-bit	i16  	u16                 // 64-bit	___ 	f64 // double precision
    // 32-bit	i32 	u32 (standard choice for integer)

    // types are declared with ':' after the variable name, reads nicer than c/c++ bool foo = true;
    let bool_value: bool = true; // rust_fmt expects snake case for most variables
    println!("a boolean value: {}", bool_value);
    let x: f32 = 3.14;
    println!("single precision value: {}", x);

    // Rust has char types, that are Unicode by default
    let z = 'z'; // char literals use single quotes
    let my_string = "string literal"; // string use double quotes (!!!)
    let heart_eyed_cat = '😻';
    println!(
        "{}, {}, {}, length of {}",
        z,
        my_string,
        heart_eyed_cat,
        my_string.len()
    );
    // Rust has arrays, but you basically can't initialize an array in a loop
    let my_array: [i32; 6] = [0, 1, 2, 3, 4, 5];
    for i in 1..my_array.len() {
        // my_array[i] = i;
        println!("{}", my_array[i]);
    }

    // calling a function declared at bottom of file (they're not 'hoisted' but this still works)
    hello_string(my_string);
    let x = add_one(2);
    println!("this value was returned from a function: {}", x);

    // Rust has expressions that can be evaluated in the body of '{}'
    // lines ending with a ';' are considered statements,
    // lines of a function or expression not ending in a ';' are often used as way of returning a value
    let x = {
        let initial_value = 2 + 2;
        initial_value + 1 // no ';' this value will be returned and assigned to x
    };
    println!(
        "This value came from an expression that was evaluated: {}",
        x
    );
}

// Regular functions seem pretty straight forward
fn hello_string(x: &str) {
    println!("{}", x)
}

// return values are declared with '->' symbol
fn add_one(x: i32) -> i32 {
    x + 1 // could also have said 'return x + 1;'
}
