use std::{collections::HashMap, io};

fn main() {
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line");
    let n: usize = input.trim().parse().expect("Invalid input");
    input.clear();
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line");
    let mut nums: Vec<i32> = input
        .split_whitespace()
        .map(|x| x.parse().expect("Invalid input"))
        .collect();

    let mut ans = vec![-1; n];
    let mut stack: Vec<i32> = vec![];

    let mut frequency: HashMap<i32, i32> = HashMap::new();

    for i in &nums {
        if let Some(x) = frequency.get_mut(&i) {
            *x += 1;
        } else {
            frequency.insert(*i, 1);
        }
    }

    for i in 0..n {
        while !stack.is_empty()
            && frequency
                .get(&(nums[*(stack.last().unwrap()) as usize] as i32))
                .unwrap()
                < frequency.get(&(nums[i])).unwrap()
        {
            if let Some(last) = stack.pop() {
                ans[last as usize] = nums[i];
            }
        }
        stack.push(i as i32);
    }

    println!(
        "{}",
        ans.into_iter()
            .map(|x| x.to_string())
            .collect::<Vec<String>>()
            .join(" ")
    );
}
