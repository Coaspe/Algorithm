use std::collections::BinaryHeap;
use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    // Read `n` and `k`
    let first_line = lines.next().unwrap().unwrap();
    let mut iter = first_line.split_whitespace();
    let n: usize = iter.next().unwrap().parse().unwrap();
    let k: usize = iter.next().unwrap().parse().unwrap();

    // Read `a` and `b`
    let second_line = lines.next().unwrap().unwrap();
    let a: Vec<usize> = second_line
        .split_whitespace()
        .map(|x| x.parse::<usize>().unwrap())
        .collect();

    let third_line = lines.next().unwrap().unwrap();
    let b: Vec<i64> = third_line
        .split_whitespace()
        .map(|x| x.parse::<i64>().unwrap())
        .collect();

    // Initialize `p` and `q`
    let mut p = vec![vec![]; n];
    let mut q = vec![vec![]; n];

    for i in 0..n {
        p[a[i] - 1].push(b[i]);
    }

    for i in &mut p {
        i.sort();
        for (j, &val) in i.iter().enumerate() {
            q[j].push(val);
        }
    }

    let mut pq = BinaryHeap::new();
    let mut s = 0;

    for i in &q {
        for &j in i {
            if pq.len() < k {
                s += j;
                pq.push(j);
            } else if pq.peek().unwrap() > &j {
                s += j - pq.pop().unwrap();
                pq.push(j);
            }
        }

        // Output results
        if pq.len() == k {
            print!("{} ", s);
        } else {
            print!("-1 ");
        }
    }
}
