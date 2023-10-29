func solution(_ string: String, _ bomb: String) -> String {
    var stack = [Character]()

    for s in string {
        stack.append(s)

        if s == bomb.last, String(stack.suffix(bomb.count)) == bomb {
            stack.removeLast(bomb.count)
        }
    }

    return stack.isEmpty ? "FRULA" : String(stack)
}

if let string = readLine(), let bomb = readLine() {
    print(solution(string, bomb))
}
