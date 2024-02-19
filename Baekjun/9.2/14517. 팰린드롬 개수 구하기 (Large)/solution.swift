let S = Array(readLine()!)
let MOD = 10007
var dp = Array(repeating: Array(repeating: 0, count: S.count), count: S.count)

func solve(_ s: Int, _ e: Int) -> Int {
    if s > e {
        return 0
    }
    if s == e {
        return 1
    }
    if dp[s][e] != 0 {
        return dp[s][e]
    }

    dp[s][e] = (solve(s, e-1) + solve(s + 1, e)-solve(s + 1, e-1)) % MOD
    
    if dp[s][e] < 0 {
        dp[s][e] += MOD
    }
    
    if S[s] == S[e] {
        dp[s][e] = (dp[s][e] + solve(s + 1, e-1) + 1) % MOD
    }

    return dp[s][e]
}

print(solve(0, S.count-1))
