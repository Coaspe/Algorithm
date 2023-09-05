let n = Int(readLine()!)!
var arr = readLine()!.split(separator:" ").compactMap{Int($0)}
var mapNum = [1:0, 2:0, 3:0]

for a in arr {
    mapNum[a]! += 1
}

var dp:[[[Float]]] = Array(repeating:Array(repeating: Array(repeating: 0.0, count: n+1), count: n+1), count:n+1)

for i in 0...n {
    for j in 0...n {
        for k in 0...n {
            let zero = n - i - j - k
            if zero == n || zero < 0 {
                continue
            }

            var val: Float = 1.0
            if i > 0 {
                val += (i / n) * dp[i-1][j+1][k] 
            }
            if j > 0 {
                val +=  (j / n) * dp[i][j-1][k+1]
            }
            if k > 0 {
                val += (k / n) * p[i][j][k-1]
            }

            dp[i][j][k] = val / (1 - Float(zero/n))
        }
    }
}
print(String(format: "%.10f", dp[mapNum[3]!][mapNum[2]!][mapNum[1]!]))
