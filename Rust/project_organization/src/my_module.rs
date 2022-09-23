// This is a basic module (just a file), my_module
// code within a module is private by default
pub fn add(x: i32, y: i32) -> i32 { // add 'pub' to export the function
    println!("Hello from pub fn add in mY_module"); // this fn will be accessed when imported
    return internal_add(x, y);
}

fn internal_add(x: i32, y: i32) -> i32 { // this fn will not be accessible when imported
    println!("Hello from fn internal_add in mY_module");
    return x + y;
}