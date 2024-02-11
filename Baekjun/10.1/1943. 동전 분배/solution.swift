for _ in 0..<3 {
    let N = Int(readLine()!)!
    var coins: [Int: Int] = [:]
    var T = 0
    
    for _ in 0..<N {
        let ab = readLine()!.split(separator: " ").compactMap { Int($0) }
        coins[ab[0]] = ab[1]
        T += ab[0] * ab[1]
    }
    
    if T % 2 == 1 {
        print(0)
        continue
    }
    
    T /= 2
    var dp = [1] + Array(repeating: 0, count: T)
    
    for (coin, num) in coins {
        for m in stride(from: T, through: coin, by: -1) {
            if dp[m - coin] == 1 {
                for j in 0..<num {
                    if m + coin * j <= T {
                        dp[m + coin * j] = 1
                    }
                }
            }
        }
    }
    
    print(dp.last!)
}
