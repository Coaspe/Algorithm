let NK = readLine()!.split(separator: " ").compactMap {Int($0)}

let N = NK[0], K = NK[1]
let P = readLine()!.split(separator: " ").compactMap {Int($0)}
var c = P[0] % K
var ans = 0

for i in 1..<N {
    ans += K / 2 >= c ? c : K-c
    c = (c + P[i]) % K
}

if (c == 0) {
    print(ans)
} else {
    print("blobsad")
}