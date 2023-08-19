let W1 = readLine()!.map { String($0) }
let W2 = readLine()!.map { String($0) }
let L1 = W1.count, L2 = W2.count
var dp = Array(repeating: Array(repeating: 0, count: L2+1), count: L1+1)

for i in 1...L1 {
    for j in 1...L2 {
        if W1[i-1] == W2[j-1] {
            dp[i][j] = dp[i-1][j-1] + 1
        } else {
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        }
    }
}

print(dp.last!.last!)
