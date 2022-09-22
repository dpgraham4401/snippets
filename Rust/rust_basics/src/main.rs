// Rust has a strange syntax that feels like a cross between c++ and JavaScript, so beware

// 'main' is always the entrypoint for binary applications.
fn main() {
    // MUTABILITY
    // variables declared with let are immutable by default
    let x = 10;
    println!("x starts out as {}", x);
    // x = x + 1 // this will not even compile in rust
    // you can change that with 'mut' keyword
    let mut y = 41;
    y = y + 1; // this can be done with mut keyword
    println!("{}", y);
    // things can be overshadowed however if we use the let word again
    let x = "string";
    // 'const' keyword means it is never mutable
    println!("x is now {}", x);

    // TYPES
    // rust is a statically typed language and has an overkill of types
    // bits     signed  unsigned
    // 8-bit	i8  	u8
    // 16-bit	i16  	u16
    // 32-bit	i32 	u32 // standard choice for integer

    // floats, all floats are unsigned
    // 32-bit	___ 	f32 // single precision
    // 64-bit	___ 	f64 // double precision

    // type is declared with ':' after the variable name
    let bool_value: bool = true; // rust is pretty opinionated about variables should be snake case
    println!("a boolean value: {}", bool_value);
    let x: f32 = 3.14;
    println!("single precision value: {}", x);

    // primitive CHARACTERS and STRINGS
    // Rust has char types, that are unicode by default
    let z = 'z'; // char literals use single quotes
    let my_string = "string literal"; // string literals use double quotes (!!!)
    let heart_eyed_cat = '😻';
    println!(
        "{}, {}, {}, length of {}",
        z,
        my_string,
        heart_eyed_cat,
        my_string.len()
    );
    // I'll cover strings in more depth in a separate snippet

    // ARRAYS
    // Rust has arrays, but you basically can't initialize an array in a loop
    let my_array: [i32; 6] = [0, 1, 2, 3, 4, 5];
    for i in 1..my_array.len() {
        // my_array[i] = i;
        println!("{}", my_array[i]);
    }

    // FUNCTIONS and EXPRESSIONS
    // calling a function declared at bottom of file (i guess they're 'elevated')
    hello_string(my_string);
    let x = add_one(2);
    println!("this value was returned from a function: {}", x);

    // Rust has expressions that can be evaluated in the body of '{}'
    // lines ending with a ';' are considered statements,
    // you can think of a line of a function or expression not ending in a ';' to be a return statement
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
