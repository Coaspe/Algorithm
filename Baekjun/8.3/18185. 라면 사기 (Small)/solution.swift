if let N = Int(readLine()!) {
    let buf: [Int] = readLine()!.split(separator:" ").compactMap {Int($0)}
    var arr: [Int] = Array(repeating: 0, count: N+2)
    var ans = 0
  
    for i in 0..<N {
      arr[i] = buf[i]
    }
  
    for i in 0..<N {
      if arr[i+1] > arr[i+2] {
        var c5 = min(arr[i], arr[i+1] - arr[i+2])
        ans += c5 * 5
        arr[i] -= c5
        arr[i + 1] -= c5

        var c7 = min(arr[i], arr[i+1], arr[i+2])
        ans += c7 * 7
        arr[i] -= c7
        arr[i+1] -= c7
        arr[i+2] -= c7
      } else {
        var c7 = min(arr[i], arr[i+1])
        ans += c7 * 7
        arr[i] -= c7
        arr[i+1] -= c7
        arr[i+2] -= c7

        var c5 = min(arr[i], arr[i+1])
        ans += c5 * 5
        arr[i] -= c5
        arr[i+1] -= c5
        
      }
      ans += 3*arr[i]
    }

  print(ans)
}