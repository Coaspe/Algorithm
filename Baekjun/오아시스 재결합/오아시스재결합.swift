var stack: [(Int, Int)] = []
var nums: [Int] = []
var n = Int(readLine()!)
var ans = 0

for _ in 0..<n! {
    if let val = readLine() {
        nums.append(Int(val)!)
    }
}

for i in 0..<n! {
    while !stack.isEmpty && nums[i] > stack[stack.count-1].0 {
        ans += stack.popLast()!.1
    }
    if stack.isEmpty {
        stack.append((nums[i], 1))
        continue
    }
    
    if stack[stack.count-1].0 == nums[i] {
        let cnt = stack.popLast()!.1
        ans += cnt
        
        if !stack.isEmpty {
            ans += 1
        }
        
        stack.append((nums[i], cnt + 1))
    } else {
        ans += 1
        stack.append((nums[i], 1))
    }
}

print(ans)
