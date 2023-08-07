import Foundation

class Solution {
    func minEatingSpeed(_ piles: [Int], _ h: Int) -> Int {
        var left = 1
        var right = piles.max() ?? 1

        while left < right {
            let middle = (left + right) / 2
            var hourSpent = 0

            for pile in piles {
                hourSpent += Int(ceil(Double(pile) / Double(middle)))
            }

            if hourSpent <= h {
                right = middle
            } else {
                left = middle + 1
            }
        }

        return right
    }
}
