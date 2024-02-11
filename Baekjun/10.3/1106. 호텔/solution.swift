let CN = readLine()!.split(separator: " ").map { Int($0)! }
let C = CN[0], N = CN[1]
let MAX = 1000000
var hotel: [[Int]] = [[0, 0]]
for _ in 0..<N {
    hotel.append(readLine()!.split(separator: " ").map { Int($0)! })
}

var dp = Array(repeating: Array(repeating: MAX, count: C + 1), count: N + 1)

for i in 1..<N + 1 {
    let cost = hotel[i][0]
    let customer = hotel[i][1]
    for j in 1..<C + 1 {
        dp[i][j] = dp[i - 1][j]
        var k = 0
        while true {
            if j - k * customer <= 0 {
                dp[i][j] = min(dp[i][j], k * cost)
                break
            }
            dp[i][j] = min(dp[i][j], dp[i - 1][j - k * customer] + k * cost)
            k += 1
        }
    }
}

print(dp.last!.last!)
