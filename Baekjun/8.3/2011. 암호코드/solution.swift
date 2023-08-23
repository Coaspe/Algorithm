import Foundation

if let input = readLine() {
    let num = Array(input).map { Int(String($0))! }

    if num[0] == 0 {
        print(0)
        exit(0)
    }

    let N = num.count
    var dp = [Int](repeating: 0, count: N)

    if N == 1 {
        print(N)
        exit(0)
    }

    dp[0] = 1
    dp[1] = (10 <= num[0] * 10 + num[1]) && (num[1] != 0) ? 1 : 2

    for i in 2..<num.count {
        if num[i] > 0 {
            dp[i] = dp[i - 1]
        }
        if 10 <= num[i - 1] * 10 + num[i] && num[i - 1] * 10 + num[i] <= 26 {
            dp[i] += dp[i - 2]
        }
    }

    print(dp[num.count - 1] % 1000000)
}