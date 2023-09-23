let N = Int(readLine()!)!
let A = readLine()!.split(separator: " ").compactMap { Int($0) }

var left = Array(repeating: 0, count: N+1)
var total = 0
var ans = 0
var cnt = Array(repeating: 0, count: N+1)

for a in A {
    cnt[a] += 1
}

for a in A {
    ans += total - left[a] * (cnt[a] - left[a])
    total -= left[a] * (cnt[a] - left[a])
    left[a] += 1
    total += left[a] * (cnt[a] - left[a])
}

print(ans)
