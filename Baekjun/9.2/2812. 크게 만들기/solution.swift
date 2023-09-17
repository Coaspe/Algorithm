let NK = readLine()!.split(separator: " ").compactMap { Int($0) }
var N = NK[0], K = NK[1]
let k = K
var num = Array(readLine()!).map { Int(String($0))! }

var stack: [Int] = []

for i in 0 ..< N {
    while K > 0 && !stack.isEmpty && stack.last! < num[i] {
        var _ = stack.popLast()
        K -= 1
    }
    stack.append(num[i])
}

print(stack[0 ..< (N - k)].map { String($0) }.joined())