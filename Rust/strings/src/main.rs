// Rust has many types of strings, this focuses more on common usage
fn main() {
    let _a : char= 'a'; // In rust, single quotes are reserved for chars, double for everything else
    let mut a_str: &str = "a string slice"; // a &str denotes a string slice, the most primitive string
    // str is an immutable1 sequence of UTF-8 bytes,
    // a &str consist of 2 parts, a pointer and length, it's usually seen in borrowed form (with the '&' before 'str')
    println!("{:p} address of initial string", a_str);
    a_str = "another string"; // when we assign a new value, the value of the pointer is modified
    println!("{:p} address post mutate", a_str);

    // you can think of a 'string slice' as "a view into some slice of data"
    // a "string literal" is one that is hard coded somewhere in the program, it's a slice that's statically allocated
    dbg!(a_str);

    // the second, and more useful of strings is String
    let b = String::from(a_str); // a string literal, created from a &str
    // use a String if you need to own your data and/or make modifications
    // use &str if you want an immutable, hard coded string that won't change and you let functions borrow

    // strings are really a wrapper around a rust collection Vec<u8>, they share many behaviors

    // Rust strings don't inherently support indexing string characters,
    println!("{}", b.len()); // all strings are, by default, UTF-8 encoded,
    // The length will return the number of bytes, with unicode, is not necessarily the number of characters

    let c = String::from("هِجَائِي"); // for example this arabic
    println!(" for example, this arabic, {}, has length {}", c, c.len());
    // We can iterate over the characters with the .chars() method
    for i in c.chars(){
        println!("{}", i);
    }
    // we can get the number of chars from a string,
    println!("{}", c.chars().count()); // I don't think this is a recommended operation, don't see better way

    let string1 = String::from("hello, ");
    let string2 = String::from("World!");
    // we can concatenate string 2 ways
    let string3 = string1 + &string2; // There's a catch, this invalidates string1 (!!!)
    println!("string3: {}", string3); // essentially string1 is 'moved' into the add function,
    println!("string2: {}", string2); // string2 is borrowed by reference, so still usable
    // println!("{}", string1); // this will throw a compile time error


    let string4 = String::from("hello, ");
    let string5 = String::from("World!");
    // the 2nd option (better), use format!
    let mut string6 = format!("{}{}", string4, string5);
    println!("string6 = string 4 + string 5: {}", string6); // we have easy control, arguably more readable
    println!("string4: {}", string4); // string4 still valid
    println!("string5: {}", string5); // string5 also still valid, yay!

    // strings have a couple useful methods I should know
    let new_string = String::new(); // this will initialize an empty string
    println!("new_string: {}", new_string);

    let to_string_string = a_str.to_string(); // this does the same as String::from(&str)
    println!("string from &str.to_string() method: {}", to_string_string);

    let replace_string = string6.replace("hello", "GoodBye"); // case sensitive replace all occurrences
    println!("replace string6's \"hello\": {}", replace_string);

    string6.push('h'); // a string needs to be mutable (of course)
    println!("push a single char to end {}", string6);

    let split_ws_string= string6.split_whitespace(); // returns a :SplitWhitespace
    for i in test { // we can iterate through split_ws_string
        println!("{}", i);
    }
    // there's other methods outside this handful
}
