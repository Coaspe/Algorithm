func solution() {
    let inputWN = readLine()!.split(separator: " ").map { Int($0)! }
    let w = inputWN[0]
    let n = inputWN[1]
    let A = readLine()!.split(separator: " ").map { Int($0)! }

    var dp: [Bool] = Array(repeating: false, count: w)
    for i in 0..<n {
        for j in i+1..<n {
            if A[i] + A[j] < w && dp[w - A[i] - A[j]] {
                print("YES")
                return
            }
        }
        
        for j in 0..<i {
            if A[i] + A[j] < w {
                dp[A[i] + A[j]] = true
            }
        }
    }       
    print("NO")
}

solution()