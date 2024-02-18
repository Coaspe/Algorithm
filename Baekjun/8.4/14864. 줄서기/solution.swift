func solution() {
    let NM = readLine()!.split(separator: " ").compactMap { Int($0) }
    let N = NM[0], M = NM[1]
    var cards = Array(1 ... N)

    if M == 0 {
        print(cards.map { String($0) }.joined(separator: " "))
        return
    }

    for _ in 0 ... M - 1 {
        let xy = readLine()!.split(separator: " ").compactMap { Int($0) }
        cards[xy[0] - 1] += 1
        cards[xy[1] - 1] -= 1
    }

    let cardsSet = Set(cards)

    if cardsSet.count != N {
        print(-1)
        return
    }

    for i in cardsSet {
        if i < 1 || i > N {
            print(-1)
            return
        }
    }

    print(cards.map { String($0) }.joined(separator: " "))
}

solution()
