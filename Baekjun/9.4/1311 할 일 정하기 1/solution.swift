let N = Int(readLine()!)!

var cost:[[Int]] = []

for _ in 0..<N {
    cost.append(readLine()!.split(separator: " ").compactMap{Int($0)})
}
 
let MAX = 10000
var dp = Array(repeating:MAX, count: (1 << N))

dp[0] = 0

for i in 0..<(1 << N) {
    let cnt = i.bitWidth
    for j in 0..<N {
        if i & (1 << j) {
            continue
        }
        dp[i | (1 << j)] = min(dp[i | (1 << j)], dp[i] + cost[cnt][j])
    }
}

print(dp.last!)