func solution() -> Void {
    let N = Int(readLine()!)!

    var dp: [[Int]] = Array(repeating: [0, 0], count: N)
    var arr = [Int(readLine()!)!]

    if N == 1 { 
        print(arr[0])
        return
    }
  
    arr.append(Int(readLine()!)!)
  
    dp[0][1] = arr[0]
    dp[1][0] = arr[0]
    dp[1][1] = arr[0] + arr[1]

    for i in 2..<N {
        arr.append(Int(readLine()!)!)
        dp[i][0] = dp[i-1].max()!
        dp[i][1] = max(dp[i-1][0], dp[i-2][0] + arr[i-1]) + arr[i]
    }

    print(dp.last!.max()!)
}

solution()