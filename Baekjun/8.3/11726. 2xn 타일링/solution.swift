let N = Int(readLine()!)!

var dp: (Int, Int) = (1, 2)
if N <= 2 {
  print(N)
} else {
  for _ in 1...N-2 {
      dp = (dp.1, (dp.0 + dp.1)%10007)
  }
  print(dp.1) 
}