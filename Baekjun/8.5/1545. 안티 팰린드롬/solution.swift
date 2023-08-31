func solution(){
  var S = readLine()!.map { Character(String($0)) }
  
  let n = S.count
  var i:Int = n / 2 - 1, j:Int = n / 2 + (n % 2 == 1 ? 1 : 0)
  
  S.sort()
  
  while j < n && i > -1 {
      var idx = j
      if S[i] == S[idx] {
          while S[i] == S[idx] {
              idx += 1
              if idx == n {
                  print(-1)
                  return
              }
          }
          S.swapAt(j, idx)
      }
      i -= 1
      j += 1
  }
  
  print(String(S))
}
solution()