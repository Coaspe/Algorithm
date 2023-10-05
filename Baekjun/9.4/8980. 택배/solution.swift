let NC = readLine()!.split(separator: " ").compactMap { Int($0) }
let N = NC[0], C = NC[1]
let M = Int(readLine()!)!
var q: [[Int]] = []

for _ in 0 ..< M {
    q.append(readLine()!.split(separator: " ").compactMap { Int($0) })
}

q.sort {
    return $0[1] < $1[1]
}

var capacity = Array(repeating: C, count: N)
var ans = 0

for i in 0 ..< M {
    var a = q[i][0], b = q[i][1], n = q[i][2]
    var _min = min(C, n)

    for j in a ..< b {
        _min = min(_min, capacity[j])
    }

    for j in a ..< b {
        capacity[j] -= _min
    }

    ans += _min
}

print(ans)
