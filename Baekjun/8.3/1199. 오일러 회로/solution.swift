func solution() {
    let N = Int(readLine()!)!

    var degree = Array(repeating: 0, count: N)
    var visit = Array(repeating: Array(repeating: 0, count: N), count: N)
    var graph:[[Int:Int]] = []

    for i in 0..<N {
        var lst:[Int:Int] = [:]

        if let input = readLine() {
            let numbers = input.split(separator: " ").compactMap { Int($0) }

            for (idx, j) in numbers.enumerated() {
                if j != 0 {
                    degree[i] += j
                    visit[i][idx] = j
                    lst[idx] = 1
                }
            }
        }

        graph.append(lst)
    }

    for i in 0..<N {
        if degree[i] % 2 == 1 {
            print(-1)
            return
        }
    }

    var answer:[Int] = []
    var stack:[Int] = [0]

    while !stack.isEmpty {

        if let current = stack.last, !graph[current].isEmpty {
            let (key, _) = graph[current].first!

            visit[current][key] -= 1
            visit[key][current] -= 1
            degree[current] -= 1
            degree[key] -= 1

            if visit[current][key] == 0 {
                graph[current].removeValue(forKey: key)
                graph[key].removeValue(forKey: current)
            }

            stack.append(key)
        } else {
            answer.append(stack.popLast()! + 1)
        }
    }

    for i in 0..<N {
        if degree[i] > 0 {
            print(-1)
            return
        }
    }

    print(answer.map { String($0)}.joined(separator: " "))
}

solution()
