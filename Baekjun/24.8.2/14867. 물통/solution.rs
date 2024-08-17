use std::collections::{HashSet, VecDeque};
use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let values: Vec<i32> = input
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let (a_max, b_max, target_a, target_b) = (values[0], values[1], values[2], values[3]);

    let mut visited = HashSet::new();
    let mut queue = VecDeque::new();

    visited.insert((0, 0));
    queue.push_back((0, 0, 0));

    while let Some((a, b, c)) = queue.pop_front() {
        if a == target_a && b == target_b {
            println!("{}", c);
            return;
        }

        // Closure to add new state
        let mut add = |new_a, new_b| {
            if visited.insert((new_a, new_b)) {
                queue.push_back((new_a, new_b, c + 1));
            }
        };

        // Possible moves
        add(0, b);                         // Empty A
        add(a, 0);                         // Empty B
        add(a_max, b);                     // Fill A
        add(a, b_max);                     // Fill B
        add(std::cmp::min(a_max, a + b), std::cmp::max(0, b - (a_max - a))); // Pour B into A
        add(std::cmp::max(0, a - (b_max - b)), std::cmp::min(b_max, a + b)); // Pour A into B
    }

    println!("-1");
}
