let N = Int(readLine()!)!

var arr: [[Int]] = []

for _ in 1...N {
    arr.append(readLine()!.split(separator: " ").compactMap{Int($0)})
}

var dp: [[Int]] = Array(repeating: Array(repeating:0, count: N), count: N)

dp[0][0] = arr[0][0]

for i in 1..<N {
    for j in 0...i {
        if i >= 1 {
            dp[i][j] = max(dp[i][j], dp[i-1][j])
        }
        if i >= 1 && j >= 1 {
            dp[i][j] = max(dp[i][j], dp[i-1][j-1])
        }
        dp[i][j] += arr[i][j]
    }
}

print(dp.last!.max()!)