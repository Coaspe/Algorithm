class Solution {
    func subarraySum(_ nums: [Int], _ k: Int) -> Int {
        var prefixSumCounts: [Int: Int] = [0: 1]
        var currentPrefixSum = 0
        var totalCount = 0
        
        for num in nums {
            currentPrefixSum += num
            
            if let count = prefixSumCounts[currentPrefixSum - k] {
                totalCount += count
            }
            
            prefixSumCounts[currentPrefixSum, default: 0] += 1
        }
        
        return totalCount
    }
}
