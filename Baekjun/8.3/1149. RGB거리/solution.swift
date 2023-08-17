let N = Int(readLine()!)!
var dp:[[Int]] = Array(repeating: Array(repeating: 0, count: 3), count: N)
let abc = readLine()!.split(separator: " ").compactMap {Int($0)}

dp[0][0] = abc[0]
dp[0][1] = abc[1]
dp[0][2] = abc[2]


for i in 1...N-1 {
    let abc = readLine()!.split(separator: " ").compactMap {Int($0)}

    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + abc[0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + abc[1]
    dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + abc[2]
}

print(dp.last!.min()!)