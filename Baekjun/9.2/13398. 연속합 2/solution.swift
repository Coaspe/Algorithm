let N = Int(readLine()!)!
let arr = readLine()!.split(separator: " ").compactMap { Int($0) }

var dp = Array(repeating: Array(repeating: 0, count: 2), count: N)

dp[0][0] = arr[0]
var ans = arr[0]

for i in 1 ..< N {
    dp[i][0] = max(dp[i - 1][0] + arr[i], arr[i])
    dp[i][1] = max(dp[i - 1][1] + arr[i], dp[i - 1][0])
    ans = max(ans, dp[i][0], dp[i][1])
}

print(ans)
