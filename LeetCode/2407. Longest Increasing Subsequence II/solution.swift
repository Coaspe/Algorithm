class Solution {
    func lengthOfLIS(_ nums: [Int], _ k: Int) -> Int {
        var N = nums.max()!
        var treeSize = 2*N
        
        var tree = Array(repeating: 0, count: treeSize)
        
        func update(_ i:Int, _ val:Int) {
            var i = i + N
            tree[i] = val
            
            while i > 1 {
                tree[i >> 1] = max(tree[i], tree[i^1])
                i >>= 1
            }
        }
        
        func query(_ l:Int, _ r:Int)-> Int {
            var ret = 0
            var l = l + N, r = r + N
            
            while r > l {
                if l & 1 == 1 {
                    ret = max(ret, tree[l])
                    l += 1
                }
                if r & 1 == 1 {
                    r -= 1
                    ret = max(ret, tree[r])
                }
                l >>= 1
                r >>= 1
            }
            
            return ret
        }

        var ans = 1
        for n in nums {
            var n = n - 1
            let preMax = query(max(0, n-k), n)
            ans = max(ans, preMax+1)
            update(n, preMax+1)
        }
        return ans
    }
}
