use std::io;
use std::io::BufRead;

fn main() {
    let stdin = io::stdin();
    let mut iterator = stdin.lock().lines();

    let mnl = iterator.next().unwrap().unwrap();
    let mut mnl_iter = mnl.split_whitespace();
    let m: usize = mnl_iter.next().unwrap().parse().unwrap();
    let n: usize = mnl_iter.next().unwrap().parse().unwrap();
    let l: i32 = mnl_iter.next().unwrap().parse().unwrap();

    let mut a: Vec<i32> = iterator.next().unwrap().unwrap()
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    a.sort();

    let mut ans = 0;

    for _ in 0..n {
        let line = iterator.next().unwrap().unwrap();
        let mut iter = line.split_whitespace();
        let x: i32 = iter.next().unwrap().parse().unwrap();
        let y: i32 = iter.next().unwrap().parse().unwrap();

        match a.binary_search(&x) {
            Ok(idx) => {
                if (x - a[idx]).abs() + y <= l {
                    ans += 1;
                }
            }
            Err(idx) => {
                if idx < m && (a[idx] - x).abs() + y <= l {
                    ans += 1;
                    continue;
                }
                if idx > 0 && (a[idx - 1] - x).abs() + y <= l {
                    ans += 1;
                }
            }
        }
    }

    println!("{}", ans);
}
