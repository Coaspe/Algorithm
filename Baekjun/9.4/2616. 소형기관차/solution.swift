let N = Int(readLine()!)!
var A = readLine()!.split(separator: " ").compactMap { Int($0) }
let M = Int(readLine()!)!

for i in 1 ..< N {
    A[i] += A[i-1]
}

A.insert(0, at: 0)

var dp = Array(repeating: Array(repeating: 0, count: N + 1), count: 4)

for i in 1...3 {
    for j in i * M...N {
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-M] + A[j]-A[j-M])
    }
}

print(dp.last!.last!)
