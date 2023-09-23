let N = Int(readLine()!)!
var D = Array(repeating: Array(repeating: 0, count: N), count: N)

for i in 0..<N {
    let line = readLine()!.split(separator: " ").compactMap {Int($0)}
    for j in i+1..<N {
        D[i][j] = line[j - (i+1)]
    }
}

var dp = Array(repeating: 0, count: 1 << N)

for b in 0..< (1<<N) {
    var l = -1
    for i in 0..<N {
        if !(b & (1 << i)) {
            l = i
            break
        }
    }

    for i in 0..<N {
        if l != i && !(b & (1 << i)) {
            nb = b | (1 << l)
            nb |= (1 << i)

            dp[nb] = max(dp[nb], dp[b] + D[l][i])
        }
    }
}

print(dp.last!)