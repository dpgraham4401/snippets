use std::process::ExitCode;
use clap::{ArgMatches, Command, Subcommand};
use super::commands;

#[derive(Subcommand, Debug)]
#[command(version, author, about, arg_required_else_help = true)]
pub enum LkjCommands {
    // eventually can move these into the appropriate commands modules
    // to avoid the massive enum of options as the CLI grows
    /// add two integers together
    Add {
        num1: i32,
        num2: i32,
    },
    /// remove one integer from another? IDK, doesn't matter
    Rm {
        num1: i32,
        num2: i32,
    },
}

// based on the subcommand passed, we retrieve the correct function to run from the commands module
fn get_run_subcommand(cmd: &str) -> Option<fn(&ArgMatches)> {
    let f = match cmd {
        "add" => commands::add::run,
        "rm" => commands::rm::run,
        _ => return None
    };
    Some(f)
}

pub fn run() -> ExitCode {
    // instead of having the top level command in a struct, we use the builder API
    let lkj: Command = Command::new("lkj");
    // then attach the sub-commands created with the derive API
    let lkj = LkjCommands::augment_subcommands(lkj);

    // since we're not using the derive API, we parse all args into an ArgMatches struct from clap
    let args: ArgMatches = lkj.get_matches();
    // parse the sub-command and argument,
    // we'll use the sub-command to decide which sub-command to run
    // and the the arguments will be passed to said command (from commands module)
    let (cmd, sub_args) = match args.subcommand() {
        Some((cmd, args)) => (cmd, args),
        _ => {
            return ExitCode::FAILURE
        }
    };

    let run_subcommand_fn = match get_run_subcommand(cmd) {
        Some(f) => f,
        None => { return ExitCode::FAILURE}
    };
    // all of the run functions in the commands module have the same signature
    // run functions are in charge of parsing the args and calling passing to the Ops module in the library.
    // This way we can grow the CLI in a scalable way and avoid having to add arguments like so...
    // https://github.com/cnpryer/huak/blob/45e9785aa53d736667b68ac364ab243ac7f64308/src/bin/huak/commands/mod.rs#L119
    // which looks OK for now, but I think as the CLI grows I think this will become unmanageable.
    run_subcommand_fn(sub_args);

    ExitCode::SUCCESS
}