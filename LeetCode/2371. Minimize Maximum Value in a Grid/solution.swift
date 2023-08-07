import Foundation

class Solution {
    func minScore(_ grid: [[Int]]) -> [[Int]] {
        let m = grid.count, n = grid[0].count
        var grid1 = Array(repeating: Array(repeating: 0, count: n), count: m)
        var rowMins = Array(repeating: 0, count: m), colMins = Array(repeating: 0, count: n)
        
        var aux:[(Int, Int, Int)] = []
        
        for i in 0..<m {
            for j in 0..<n {
                grid1[i][j] = grid[i][j]
                aux.append((grid[i][j], i, j))
            }
        }
        aux.sort { $0.0 < $1.0 }
        
        for val in aux {
            var (_, i, j) = val
            grid1[i][j] = max(rowMins[i], colMins[j]) + 1
            
            rowMins[i] = max(rowMins[i], grid1[i][j])
            colMins[j] = max(colMins[j], grid1[i][j])
        }
        return grid1
    }
}
