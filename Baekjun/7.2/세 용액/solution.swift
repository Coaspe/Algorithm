let N = Int(readLine()!)!
let arr = readLine()!.split(separator: " ").map { Int(String($0))! }.sorted()

var cand: [Int] = [Int.max, 0, 0, 0]

loop: for i in 0 ... N-3 {
    var l = i + 1
    var r = N - 1
    
    while r > l {
        var sum = arr[l] + arr[i] + arr[r]
        if abs(sum) < cand[0] {
            cand[0] = abs(sum)
            cand[1] = arr[i]
            cand[2] = arr[l]
            cand[3] = arr[r]
        }
        
        if sum > 0 {
            r -= 1
        } else if sum < 0 {
            l += 1
        } else {
            break loop
        }
    }
}

print(cand[1...3].map{String($0)}.joined(separator: " "))

