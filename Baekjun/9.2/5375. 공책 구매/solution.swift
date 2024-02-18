var T = Int(readLine()!)!

while T > 0 {
    T -= 1

    let NM = readLine()!.split(separator: " ").compactMap { Int($0) }
    let N = NM[0], M = NM[1]
    var shop: [[Int]] = []

    for _ in 0 ..< M {
        shop.append(readLine()!.split(separator: " ").compactMap { Int($0) })
    }
    var dp = Array(repeating: 1000000000, count: N + 1)

    dp[0] = 0
    shop.sort { f, s in
        f[1] < s[1]
    }

    for S in shop {
        let s = S[0], p = S[1], o = S[2]
        for j in stride(from: N-1, to: -1, by: -1) {
            let num = min(N, j + s)
            dp[num] = min(dp[num], dp[j] + p * (num-j) + o)
        }
    }

    print(dp.last!)
}
