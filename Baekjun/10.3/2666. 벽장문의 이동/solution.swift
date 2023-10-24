let N = Int(readLine()!)!
let FS = readLine()!.split(separator: " ").compactMap { Int($0) }
let D = Int(readLine()!)!
var Q: [Int] = []

for _ in 0 ..< D {
    Q.append(Int(readLine()!)!)
}

var dp = Array(repeating: Array(repeating: Array(repeating: -1, count: N+1), count: N+1), count: D)

func solve(_ d: Int, _ door1: Int, _ door2: Int) -> Int {
    if d == D {
        return 0
    }

    if dp[d][door1][door2] != -1 {
        return dp[d][door1][door2]
    }
    let val = Q[d]

    let open1 = solve(d+1, val, door2)+abs(val - door1)
    let open2 = solve(d+1, door1, val)+abs(val - door2)

    dp[d][door1][door2] = min(open1, open2)

    return dp[d][door1][door2]
}

print(solve(0, FS[0], FS[1]))
