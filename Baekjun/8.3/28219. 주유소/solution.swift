let Nk = readLine()!.split(separator: " ").compactMap { Int($0) }
let N = Nk[0]
let k = Nk[1]

var graph = Array(repeating: [] as [Int], count: N + 1)

for _ in 0 ..< N - 1 {
    let ab = readLine()!.split(separator: " ").compactMap { Int($0) }
    let a = ab[0], b = ab[1]
    graph[a].append(b)
    graph[b].append(a)
}

var stack: [Int] = [1]
var visited: [Int] = Array(repeating: 0, count: N + 1)
var dist: [Int] = Array(repeating: 0, count: N + 1)
var ans = 0

while !stack.isEmpty {
    let node = stack.last!
    
    if visited[node] == 0 {
        visited[node] = 1
        for nextNode in graph[node] {
            if visited[nextNode] == 0 {
                stack.append(nextNode)
            }
        }
        continue
    }
    
    visited[node] = 2
    
    var dist1 = 0, dist2 = 0
    
    for nextNode in graph[node] {
        if dist1 <= dist[nextNode] {
            dist2 = dist1
            dist1 = dist[nextNode]
        } else if dist2 <= dist[nextNode] {
            dist2 = dist[nextNode]
        }
    }
    
    if k <= dist1 + dist2 {
        ans += 1
        dist[node] = 0
    } else {
        dist[node] = dist1 + 1
    }
    
    stack.popLast()
}

print(ans)
