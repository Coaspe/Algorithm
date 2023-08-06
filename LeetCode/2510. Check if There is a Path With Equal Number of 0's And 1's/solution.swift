import Foundation
struct TT: Hashable {
    let i: Int
    let j: Int
    let sum: Int
    
    init(_ i: Int, _ j: Int, _ sum: Int) {
        self.i = i
        self.j = j
        self.sum = sum
    }
    
    func hash(into hasher: inout Hasher) {
        hasher.combine(i)
        hasher.combine(j)
        hasher.combine(sum)
    }
}

class Solution {
    func isThereAPath(_ grid: [[Int]]) -> Bool {
        var cache: [TT : Bool] = [:]
        
        func remap(_ i: Int, _ j: Int) -> Int {
            if grid[i][j] == 0 {
                return -1
            }
            return 1
        }

        func dp(_ i: Int, _ j: Int, _ sum: Int) -> Bool {

            let sum = sum + remap(i, j)
            
            if let ret = cache[TT(i, j, sum)]{
                return ret
            }

            if i == 0 && j == 0 {
                return sum == 0
            }

            let up = (i > 0 && dp(i - 1, j, sum))
            let left = (j > 0 && dp(i, j-1, sum))
            
            cache[TT(i, j, sum)] = up || left
            
            return up || left
        }

        let N = grid.count - 1
        let M = grid[0].count - 1

        return dp(N, M, 0)
    }
}