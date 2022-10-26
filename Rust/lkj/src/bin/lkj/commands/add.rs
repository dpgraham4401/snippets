use clap::ArgMatches;
use lkj::ops::add;

pub fn run(args: &ArgMatches) {
    let num1 = *args.get_one::<i32>("num1").unwrap();
    let num2 = *args.get_one::<i32>("num2").unwrap();
    let my_nums: &[i32] = &[num1, num2];
    add::exec(my_nums);
}