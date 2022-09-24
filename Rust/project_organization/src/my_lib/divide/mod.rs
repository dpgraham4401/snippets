// in divide/mod.rs we're defining the divide module
mod internal_divide; // first define the internal_divide sub module, (from another file)
// but don't make it public

// now we can expose aspects of our submodules in our divide module
pub use super::divide::internal_divide::int_divide as divide;