// mod.rs is where we define the my_lib module (where 'my_lib' is the name of the directory)

// the 'mod' keyword has 2 very different ways to define a module
mod multiply; // this says the module contents is in another file dir (./sub_lib.rs or ./sub_lib/mod.rs)
mod add; // these modules are declared here but aren't made public (e.i., for ../main.rs)
mod divide;

// we could also declare modules inline like this
mod my_math {
    pub use super::multiply::multiply;
    pub use super::add::add;
}


// This way, we can bring pub functions into the my_lib namespace and expose them to main.rs
pub use super::my_lib::divide::divide;
pub use super::my_lib::multiply::multiply;
pub use super::my_lib::add::add;
pub use super::my_lib::my_math::add as add_again; // we can also alias to avoid namespace conflicts
