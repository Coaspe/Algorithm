func solution() {
    let NM = readLine()!.split(separator: " ").compactMap { Int($0) }
    var N = NM[0], M = NM[1]
    var cards = Array(1 ... N)

    for _ in 0 ... M - 1 {
        var xy = readLine()!.split(separator: " ").compactMap { Int($0) }
        cards[xy[0]-1] += 1
        cards[xy[1]-1] -= 1
    }

    var cardsSet: Set = Set(cards)

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
    
    let cardStrings = cards.map { String($0) }
    let joinedCards = cardStrings.joined(separator: " ")
    
    print(joinedCards)
}

solution()
