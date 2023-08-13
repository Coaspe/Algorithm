let N = Int(readLine()!)!
let W = Int(readLine()!)!
let INF = 1_000_000_000

var cases: [(Int, Int)] = []

for _ in 0..<W {
    let ab = readLine()!.split(separator: " ").map {Int($0)}
    cases.append((ab[0]!, ab[1]!))
}

var car1 = [(1, 1)] + cases
var car2 = [(N, N)] + cases

var dp = Array(repeating: Array(repeating: INF, count: W+2), count: W+2)

func findDP(_ car1:Int, _ car2:Int, _ case1:[(Int, Int)], _ case2:[(Int, Int)]) -> Int {
    if dp[car1][car2] != INF {
        return dp[car1][car2]
    }
    
    if car1 == W || car2 == W {
        return 0
    }
    
    let nextCase = max(car1, car2) + 1
    
    let car1Dist = abs(case1[car1].0 - case1[nextCase].0) + abs(case1[car1].1 - case1[nextCase].1)
    let car2Dist = abs(case2[car2].0 - case2[nextCase].0) + abs(case2[car2].1 - case2[nextCase].1)
    
    let car1Case = car1Dist + findDP(nextCase, car2, case1, case2)
    let car2Case = car2Dist + findDP(car1, nextCase, case1, case2)
    
    dp[car1][car2] = min(car1Case, car2Case)
    
    return dp[car1][car2]
}

func findPath(_ car1:Int, _ car2:Int, _ case1:[(Int, Int)], _ case2:[(Int, Int)]) {
    if car1 == W || car2 == W {
        return
    }
    
    let nextCase = max(car1, car2) + 1
    
    let car1Dist = abs(case1[car1].0 - case1[nextCase].0) + abs(case1[car1].1 - case1[nextCase].1)
    let car2Dist = abs(case2[car2].0 - case2[nextCase].0) + abs(case2[car2].1 - case2[nextCase].1)
    
    let result1 = car1Dist + dp[nextCase][car2]
    let result2 = car2Dist + dp[car1][nextCase]
    
    if result1 < result2 {
        print(1)
        findPath(nextCase, car2, case1, case2)
    } else {
        print(2)
        findPath(car1, nextCase, case1, case2)
    }
}

print(findDP(0, 0, car1, car2))

findPath(0, 0, car1, car2)

