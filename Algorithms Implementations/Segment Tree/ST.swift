var a = readLine()!.split(separator: " ").compactMap{Int($0)}
var treeSize = ceil(log2(a.count)) + 1
var tree:[Int] = Array(repeating:0, count:1 << treeSize)
var N = a.count

func init(_ node:Int, _ start:Int,_ end:Int) {
    if start == end {
        tree[node] = a[start]
    } else {
        init(node*2, start, (start+end) / 2)
        init(node*2+1, (start+end)/2+1, end)
        tree[node] = tree[node*2]+tree[node*2+1]
    }
}

func update(_ node:Int, _ start:Int, _ end:Int, _ idx:Int, _ val:Int) {
    if idx < start || idx > end {
        return
    }

    if start == end {
        a[idx] = val
        tree[node] += val
        return
    }
    update(node*2, start, (start+end)/2, idx, val)
    update(node*2+1, (start+end)/2+1, end, idx, val)

    tree[node] = tree[node*2] + tree[node*2+1]
}

func query(_ node:Int, _ start:Int, _ end: Int, _ left:Int, _ right: Int) -> Int {
    if left > end || right < start {
        return 0
    }

    if left <= start && end <= right {
        return tree[node]
    } 

    lsum = query(2*node, start, (start+end)/2, left, right)
    rsum = query(2*node+1, (start+end)/2+1, end, left, right)

    return lsum + rsum
}