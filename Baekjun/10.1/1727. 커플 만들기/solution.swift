let NM = readLine()!.split(separator: " ").compactMap { Int($0) }
let N = NM[0], M = NM[1]

var men = [0]+readLine()!.split(separator: " ").compactMap { Int($0) }
var women = [0]+readLine()!.split(separator: " ").compactMap { Int($0) }

men.sort()
women.sort()

// dp[i][j] => i번째 남자, j번째 여자까지 봤을 때 성격의 차이의 합의 최솟값
var dp = Array(repeating: Array(repeating: 0, count: M+1), count: N+1)

for i in 1..<N+1 {
    for j in 1..<M+1 {
        dp[i][j] = dp[i-1][j-1]+abs(men[i]-women[j])

        if i > j {
            dp[i][j] = min(dp[i][j], dp[i-1][j])
        } else if i < j {
            dp[i][j] = min(dp[i][j], dp[i][j-1])
        }
    }
}

print(dp.last!.last!)
