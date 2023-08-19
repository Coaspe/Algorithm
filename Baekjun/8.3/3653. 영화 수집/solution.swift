import Foundation

class ST {
    var tree: [Int]
    let n: Int
    
    init(_ tree: [Int], _ n: Int) {
        self.tree = tree
        self.n = n
    }
    
    func build(_ arr: [Int]) {
        for i in 0 ..< arr.count {
            self.tree[self.n + i] = arr[i]
        }
        
        for i in stride(from: self.n - 1, through: 1, by: -1) {
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]
        }
    }
    
    func update(_ p: Int, _ value: Int) {
        var i = p + self.n
        self.tree[i] += value
        
        while i > 1 {
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
            i >>= 1
        }
    }
    
    func query(_ l: Int, _ r: Int) -> Int {
        var res = 0
        
        var l = l + self.n
        var r = r + self.n
        
        while r > l {
            if l & 1 == 1 {
                res += self.tree[l]
                l += 1
            }
            
            if r & 1 == 1 {
                r -= 1
                res += self.tree[r]
            }
            
            l >>= 1
            r >>= 1
        }
        
        return res
    }
}

var T = Int(readLine()!)!

while T > 0 {
    T -= 1
    
    let NM = readLine()!.split(separator: " ").compactMap { Int($0) }
    let N = NM[0]
    let M = NM[1]
    
    let treeSize = Int(pow(2, ceil(log2(Double(N + M)))))
    var tree: [Int] = Array(repeating: 0, count: 2 * treeSize)
    
    let moves = readLine()!.split(separator: " ").compactMap { Int($0) }
    
    var dvds = [Int]()
    for i in 0 ..< N {
        dvds.append(i + M)
    }
    
    let indice = Array(repeating: 0, count: M) + Array(repeating: 1, count: N)
    let st = ST(tree, treeSize)
    
    st.build(indice)
    
    var ans: [Int] = []
    var lastest = M - 1
    
    for m in moves {
        let idx = m - 1
        st.update(dvds[idx], -1)
        
        ans.append(st.query(0, dvds[idx]))
        
        dvds[idx] = lastest
        lastest -= 1
        
        st.update(dvds[idx], 1)
    }
    
    print(ans.map { String($0) }.joined(separator: " "))
}
