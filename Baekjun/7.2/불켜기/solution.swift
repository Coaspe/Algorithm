let inp = readLine()!.split(separator : " ").map{Int(String($0))!}
let N = inp[0], M = inp[1]

let dir = [(0,1),(0,-1),(1,0),(-1,0)]
var arr = Array(repeating:Array(repeating:[(Int,Int)](),count:N),count:N)
for _ in 0..<M {
    let q = readLine()!.split(separator : " ").map{Int(String($0))!}
    arr[q[0]-1][q[1]-1].append((q[2]-1,q[3]-1))
}

var light = Array(repeating:Array(repeating: false, count: N),count:N)
var visit = Array(repeating:Array(repeating: false, count: N),count:N)


var queue = [(0,0)]
light[0][0] = true
visit[0][0] = true

while !queue.isEmpty {
    
    let f = queue.removeFirst()
    
    
    for next in arr[f.0][f.1] {
        light[next.0][next.1] = true
        if visit[next.0][next.1] { continue }
        var isCanMove = false
        
        for i in 0..<4 {
            let nn = (next.0+dir[i].0,next.1+dir[i].1)
            if nn.0 >= N || nn.1>=N || nn.0<0 || nn.1<0 { continue }
            if visit[nn.0][nn.1] {
                isCanMove = true
                break
            }
        }
        if isCanMove {
            visit[next.0][next.1] = true
            queue.append(next)
        }
        
    }
    
    
    for i in 0..<4 {
        let n = (f.0+dir[i].0,f.1+dir[i].1)
        if n.0 >= N || n.1>=N || n.0<0 || n.1<0 { continue }
        if light[n.0][n.1] && !visit[n.0][n.1] {
            visit[n.0][n.1] = true
            queue.append(n)
        }
    }

}

var count = 0
for i in 0..<N {
    for j in 0..<N {
        count += (light[i][j] ? 1 : 0 )
    }
}
print(count) < <#T##()#>
