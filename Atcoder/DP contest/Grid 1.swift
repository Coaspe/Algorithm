let input = readLine()!.split(separator: " ").map{ Int($0)! }
let h = input[0], w = input[1]
let mod = 1000000007

var a = [[Character]]()
for _ in 0..<h {
    a.append(Array(readLine()!))
}

var dp = [[Int]](repeating: [Int](repeating: 0, count: w), count: h)
dp[0][0] = 1
for r in 0..<h {
    for c in 0..<w {
        if r < h - 1 && a[r + 1][c] == "." {
            dp[r + 1][c] = (dp[r + 1][c] + dp[r][c]) % mod
        }
        if c < w - 1 && a[r][c + 1] == "." {
            dp[r][c + 1] = (dp[r][c + 1] + dp[r][c]) % mod
        }
    }
}
print(dp[h - 1][w - 1])
