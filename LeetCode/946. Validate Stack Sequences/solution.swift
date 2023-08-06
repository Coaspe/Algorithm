import Foundation

class Solution {
    func validateStackSequences(_ pushed: [Int], _ popped: [Int]) -> Bool {
        var stack: [Int] = []
        var j = 0
        
        for x in pushed {
            stack.append(x)
            while !stack.isEmpty && stack.last == popped[j] {
                stack.removeLast()
                j += 1
            }
        }
        
        return popped.count == j
        
    }
}

var S = Solution()

print(S.validateStackSequences([1,2,3,4,5], [4,3, 5,1, 2]))
