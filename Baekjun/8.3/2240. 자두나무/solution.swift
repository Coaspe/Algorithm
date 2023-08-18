extension Int {
    var boolValue: Int {
        return self == 1 ? 1 : 0
    }
}

let TW = readLine()!.split(separator: " ").compactMap{Int($0)}
let T = TW[0], W = TW[1]
var dp = Array(repeating: Array(repeating: 0, count: W+1), count: T+1)

for t in 1...T {
  let loc = Int(readLine()!)!
  for w in 0..<min(t+1, W+1) {
    if w == 0 {
      dp[t][w] = dp[t-1][w] + loc.boolValue 
      continue
    }

    if (loc == 1 && w % 2 == 0) || (loc == 2 && w % 2 == 1) {
      dp[t][w] = max(dp[t-1][w-1], dp[t-1][w]) + 1
    } else {
      dp[t][w] = max(dp[t-1][w-1], dp[t-1][w])
    }
  }
}

print(dp.last!.max()!)