let NM = readLine()!.split(separator: " ").compactMap { Int($0) }
let N = NM[0], M = NM[1]

var result = 0
var tasksForWorkers: [[Int]] = []
var tasks: [Int] = Array(repeating: -1, count: M + 1)

for _ in 0 ..< N {
    tasksForWorkers.append(Array(readLine()!.split(separator: " ").compactMap { Int($0) }.suffix(from: 1)))
}

var checkedTask = Array(repeating: false, count: M + 1)

func dfs(_ worker: Int) -> Bool {
    for task in tasksForWorkers[worker] {
        if !checkedTask[task] {
            checkedTask[task] = true

            if tasks[task] == -1 || dfs(tasks[task]) {
                tasks[task] = worker
                return true
            }
        }
    }

    return false
}

for i in 0 ..< N {
    checkedTask = Array(repeating: false, count: M + 1)

    if dfs(i) {
        result += 1
    }

    checkedTask = Array(repeating: false, count: M + 1)

    if dfs(i) {
        result += 1
    }
}

print(result)
