mod cli;
mod commands;

use std::process::ExitCode;

fn main() -> ExitCode {
    // https://docs.rs/clap/latest/clap/_faq/index.html#when-should-i-use-the-builder-vs-derive-apis

    // nothing going on here, see cli.rs
    cli::run()
}
