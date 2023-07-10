import Foundation

class Solution {
    func timeTaken(arrivals: [Int], states: [Int]) -> [Int] {
        let n = arrivals.count
        var answer = Array(repeating: 0, count: n)
        
        var time = 0
        var direction = 1
        var queues: [Deque<Int>] = [Deque(), Deque()]
        
        func exhaustUntil(endTime: Int = 2 * 100000) {
            while endTime > time && queues.contains(where: { !$0.isEmpty }) {
                if queues[direction].isEmpty {
                    direction ^= 1
                }
                if let index = queues[direction].popFirst() {
                    answer[index] = time
                }
                time += 1
            }
        }
        
        for (index, (arrival, state)) in zip(arrivals.indices, zip(arrivals, states)) {
            exhaustUntil(endTime: arrival)
            if arrival > time {
                time = arrival
                direction = 1
            }
            queues[state].append(index)
        }
        
        exhaustUntil()
        
        return answer
    }
}