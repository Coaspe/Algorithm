let NM = readLine()!.split(separator: " ").compactMap { Int($0) }
var N = NM[0], M = NM[1]
let A: [Int] = readLine()!.split(separator: " ").compactMap { Int($0) }

if M >= N {
    print(N)
} else {
    var l = 1, r = A.max()! * N

    var t = r
    while r > l + 1 {
        let time: Int = (r + l) / 2

        if A.reduce(M, { result, nextValue in
            result + (time / nextValue)
        }) >= N {
            r = time
            t = min(t, r)
        } else {
            l = time
        }
    }

    var cnt: Int = A.reduce(M) { acc, cur in
        acc + (t - 1) / cur
    }

    for i in 0 ..< M {
        if t % A[i] == 0 { cnt += 1 }

        if cnt == N {
            print(i + 1)
            break
        }
    }
}
