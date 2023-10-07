let NM = readLine()!.split(separator: " ").compactMap { Int($0) }
let N = NM[0], M = NM[1]

let MIN = -1 * 3276800

// var con = Array(repeating: [0]+Array(repeating: MIN, count: M), count: N+1)
// var noncon = Array(repeating: [0]+Array(repeating: MIN, count: M), count: N+1)
//
// for i in 1 ... N {
//    let num = Int(readLine()!)!
//    for j in 1 ... min(M, (i+1) / 2) {
//        con[i][j] = max(con[i-1][j], noncon[i-1][j-1])+num
//        noncon[i][j] = max(con[i-1][j], noncon[i-1][j])
//    }
// }
//
// print(max(con.last!.last!, noncon.last!.last!))

var dp = Array(repeating: [0] + Array(repeating: MIN, count: M), count: N + 1)

var prefix: [Int] = []

for _ in 0 ..< N {
    let num = Int(readLine()!)!
    if prefix.isEmpty {
        prefix.append(num)
    } else {
        prefix.append(prefix.last! + num)
    }
}

for i in 1 ..< N + 1 {
    for j in 1 ..< M + 1 {
        dp[i][j] = dp[i-1][j]
        for k in 1 ... i {
            if k >= 2 {
                dp[i][j] = max(dp[i][j], dp[k-2][j-1] + prefix[i-1]-prefix[k-2])
            } else if k == 1, j == 1 {
                dp[i][j] = max(dp[i][j], prefix[i-1])
            }
        }
    }
}

print(dp.last!.last!)
