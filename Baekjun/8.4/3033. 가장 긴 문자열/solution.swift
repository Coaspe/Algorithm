func LCP(_ sa:[Int], _ rank:[Int], _ n:Int, _ S:String) -> [Int] {
  var lcp:[Int] = Array(repeating: 0, count: n)
  var k = 0
  let S = Array(S)

  for i in 0..<n {
    if rank[i] == 0 {
      continue
    }
    
    let j = sa[rank[i] - 1]

    if k > 0 {
      k -= 1
    }

    while j + k < n && i + k < n && S[j + k] == S[i + k] {
      k += 1
    }

    lcp[rank[i]] = k
  }
  
  return lcp
}

func MM(_ n:Int, _ S:String) -> [Int] {
  var sa:[Int] = Array(0..<n)
  var rank:[Int] = Array(S).compactMap { Int($0.asciiValue!) }
  var tmp:[Int] = Array(repeating:0, count: n)
  var k = 1

  while k <= n {
    let cmp:[Int] = (0..<n).map {
      if $0 + k < n {
        return rank[$0] << 20 | (1 + rank[$0 + k] )
      }
      return rank[$0] << 20 | 0
    }

    sa.sort {
      cmp[$0] < cmp[$1]
    }
    
    tmp[sa[0]] = 0

    for i in 1..<n {
      tmp[sa[i]] = tmp[sa[i-1]] + (cmp[sa[i]] > cmp[sa[i-1]] ? 1 : 0)
    }
    
    rank = tmp.map{$0}
    k <<= 1
    
  }
  
  return LCP(sa, rank, n, S)
}

let maxVal = MM(Int(readLine()!)!, readLine()!).max()!

if maxVal >= 2 {
  print(maxVal)
} else {
  print(0)
}
