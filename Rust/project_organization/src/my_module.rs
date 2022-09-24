// This is a basic module (just a file), my_module
// however the module is not declared here, it's declared where it's used

// code within a module is private by default
pub fn say_hello() -> String{  // add 'pub' to export the function
    return internal_string_returner();
}

fn internal_string_returner() -> String {
    return String::from("Hello from my module");
}
