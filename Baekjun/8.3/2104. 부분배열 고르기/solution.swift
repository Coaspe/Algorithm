readLine()

func solve(_ s: Int, _ e: Int) -> Int {
    if s == e {
        return A[s] * A[e]
    }
    
    let mid = (s + e) / 2
    var ret = max(solve(s, mid), solve(mid + 1, e))
    
    var left = mid, right = mid + 1
    var minVal = min(A[left], A[right])
    var _sum = A[left] + A[right]
    
    ret = max(ret, minVal * _sum)
    
    while left > s || right < e {
        if right < e && (left == s || A[left - 1] < A[right + 1]) {
            right += 1
            _sum += A[right]
            minVal = min(minVal, A[right])
        } else {
            left -= 1
            _sum += A[left]
            minVal = min(minVal, A[left])
        }
        
        ret = max(ret, minVal * _sum)
    }
    
    return ret
}

let A = readLine()!.split(separator: " ").compactMap { Int($0) }
print(solve(0, A.count - 1))
