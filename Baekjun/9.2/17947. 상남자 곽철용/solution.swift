let NMK = readLine()!.split(separator: " ").compactMap {Int($0)}
let N = NMK[0], M = NMK[1], K = NMK[2]
var card = Array(repeating: 1, count: 4*N + 1)

for _ in 0..<M {
    let ab = readLine()!.split(separator: " ").compactMap {Int($0)}
    card[ab[0]] -= 1
    card[ab[1]] -= 1
}

let cy = readLine()!.split(separator: " ").compactMap{Int($0)}

card[cy[0]] -= 1
card[cy[1]] -= 1

let gap = abs(cy[0]%K - cy[1]%K)

card = (1..<4*N+1).filter {card[$0] == 1}

for i in 0..<card.count {
    card[i] %= K
}

card.sort()

var ans = 0
var l = 0, r = 0

while (r < card.count && ans < M - 1) {

    if card[r] - card[l] <= gap {
        r += 1
    } else {
        ans += 1
        r += 1
        l += 1
    }
}

print(ans)