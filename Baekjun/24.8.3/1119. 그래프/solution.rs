use std::collections::VecDeque;
use std::io::{self, Write};

fn main() {
    let mut input = String::new();
    let stdin = io::stdin();

    stdin.read_line(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();

    let mut g: Vec<Vec<usize>> = vec![vec![]; n];

    for i in 0..n {
        input.clear();
        stdin.read_line(&mut input).unwrap();
        let line = input.trim().chars().collect::<Vec<_>>();
        for (j, &v) in line.iter().enumerate() {
            if v == 'Y' {
                g[i].push(j);
            }
        }
    }

    if n == 1 {
        println!("0");
        return;
    }

    let mut g_edges = 0;

    let mut c = vec![0; n];

    let mut groups = 0;
    for i in 0..n {
        if c[i] != 0 {
            continue;
        }

        c[i] = 1;
        groups += 1;
        g_edges += dfs(i, &g, &mut c);
    }

    if g_edges >= groups - 1 {
        println!("{}", groups - 1);
    } else {
        println!("-1");
    }
}

fn dfs(node: usize, g: &Vec<Vec<usize>>, c: &mut Vec<i32>) -> i32 {
    let mut nodes = 0;
    let mut edges = 0;
    let mut q = VecDeque::new();
    q.push_back(node);

    while let Some(n) = q.pop_front() {
        nodes += 1;
        for &next_node in &g[n] {
            edges += 1;
            if c[next_node] != 0 {
                continue;
            }
            c[next_node] = 1;
            q.push_back(next_node);
        }
    }

    if nodes == 1 {
        println!("-1");
        std::process::exit(0);
    }

    return edges / 2 - (nodes as i32 - 1);
}
