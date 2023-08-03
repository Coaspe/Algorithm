var nk: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
var N: Int = nk[0]
var K: Int = nk[1]
let n = 65536
var tree = Array(repeating: 0, count: n*2)
var dp:[Int] = []
var ans = 0

K -= 1
N -= K

for _ in 0..<K {
    let dqItem = Int(readLine()!)!
    dp.append(dqItem)
    tree[n + dqItem] += 1
}

for i in stride(from: n-1, to: 0, by: -1) {
    tree[i] = tree[i*2] + tree[i*2 + 1]
}

func update(_ A: Int)->Void {
    var val: Int = A
    while val >= 1 {
        val /= 2
        tree[val] = tree[val*2] + tree[val*2+1]
    }
}

K = (K + 2) / 2

for _ in 0..<N {
    var A = Int(readLine()!)! 
    dp.append(A)
    A += n
    tree[A] += 1
    update(A)

    A = K
    var B = 1

    while B < n {
        B *= 2

        if tree[B] < A {
            A -= tree[B]
            B += 1
        }
    }
    ans += B - n

    A = dp.removeFirst() + n
    tree[A] -= 1
    update(A)
}

print(ans)