use std::io::{self, BufRead};

fn bisect_left(arr: &[i32], x: i32) -> usize {
    let mut l: i32 = -1;
    let mut r: i32 = arr.len() as i32;

    while r > l + 1 {
        let mid = (l + r) / 2;
        if arr[mid as usize] < x {
            l = mid;
        } else {
            r = mid;
        }
    }

    r as usize
}

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    let n: usize = lines.next().unwrap().unwrap().trim().parse().unwrap();

    let mut c = Vec::with_capacity(n);
    for line in lines.take(n) {
        let line = line.unwrap();
        let mut parts = line.split_whitespace();
        let h: i32 = parts.next().unwrap().parse().unwrap();
        let k: i32 = parts.next().unwrap().parse().unwrap();
        c.push((h, k));
    }

    c.sort_by(|a, b| b.0.cmp(&a.0));
    let mut ans: Vec<i32> = vec![];
    for (_, k) in c {
        let idx = bisect_left(&ans, -k);

        if idx == ans.len() {
            ans.push(-2);
        } else {
            ans[idx] -= 1;
        }
    }

    println!("{}", ans.len());
}
