use std::io;

const MOD: i64 = 1_000_000_007;

fn go(s: usize, a: isize, b: isize, c: isize, dp: &mut Vec<Vec<Vec<Vec<i64>>>>) -> i64 {
    if s == 0 {
        return if a == 0 && b == 0 && c == 0 { 1 } else { 0 };
    }
    if a < 0 || b < 0 || c < 0 {
        return 0;
    }
    if dp[s][a as usize][b as usize][c as usize] != -1 {
        return dp[s][a as usize][b as usize][c as usize];
    }

    dp[s][a as usize][b as usize][c as usize] = 0;
    dp[s][a as usize][b as usize][c as usize] += go(s - 1, a - 1, b, c, dp);
    dp[s][a as usize][b as usize][c as usize] += go(s - 1, a, b - 1, c, dp);
    dp[s][a as usize][b as usize][c as usize] += go(s - 1, a, b, c - 1, dp);
    dp[s][a as usize][b as usize][c as usize] += go(s - 1, a - 1, b - 1, c, dp);
    dp[s][a as usize][b as usize][c as usize] += go(s - 1, a, b - 1, c - 1, dp);
    dp[s][a as usize][b as usize][c as usize] += go(s - 1, a - 1, b, c - 1, dp);
    dp[s][a as usize][b as usize][c as usize] += go(s - 1, a - 1, b - 1, c - 1, dp);
    dp[s][a as usize][b as usize][c as usize] %= MOD;
    dp[s][a as usize][b as usize][c as usize]
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let numbers: Vec<usize> = input.trim().split_whitespace()
        .map(|x| x.parse().expect("Not a number"))
        .collect();
    
    let (s, a, b, c) = (numbers[0], numbers[1] as isize, numbers[2] as isize, numbers[3] as isize);

    let mut dp = vec![vec![vec![vec![-1; c as usize + 1]; b as usize + 1]; a as usize + 1]; s + 1];

    println!("{}", go(s, a, b, c, &mut dp));
}
