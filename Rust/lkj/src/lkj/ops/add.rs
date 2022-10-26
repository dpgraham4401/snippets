pub fn exec(numbers: &[i32]) {
    println!("exec function from lkj::ops::add");
    let mut sum: i32 = 0;
    for number in numbers {
        sum += number;
    }
    println!("Sum: {}", sum);
}