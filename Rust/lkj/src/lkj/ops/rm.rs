pub fn exec(numbers: &[i32]) {
    println!("exec function from lkj::ops::rm");
    let mut result: i32 = numbers[0];
    let remain_number = &numbers[1..];
    for number in remain_number {
        result -= number;
    }
    println!("Result: {}", result);
}
