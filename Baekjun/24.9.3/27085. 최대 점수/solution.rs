use std::io::{self, BufRead};
fn main() {
    let stdin = io::stdin();
    let mut iterator = stdin.lock().lines();

    // Read the first line and parse N and S
    let first_line = iterator.next().unwrap().unwrap();
    let mut split = first_line.split_whitespace();
    let n: usize = split.next().unwrap().parse().unwrap();
    let s: usize = split.next().unwrap().parse().unwrap();

    // Read the second line and parse it into an array
    let second_line = iterator.next().unwrap().unwrap();
    let arr: Vec<i64> = second_line
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    let mut l = (s - 2) as isize;
    let mut r = s;

    let mut max_score = 0;
    loop {
        let (rm, ridx) = right(&arr, max_score, r);
        let (lm, lidx) = left(&arr, rm, l);

        if lm == max_score {
            break;
        }

        max_score = lm;

        l = lidx;
        r = ridx;
    }
    println!("{}", max_score)
}