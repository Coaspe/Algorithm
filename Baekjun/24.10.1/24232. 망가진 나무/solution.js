const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");
let line = 0

const N = Number(input[line++])

const G = Array.from(Array(N+1), ()=>[])

for (let i = 0; i < N-1; i++) {
    const [a, b] = input[line++].split(" ").map(Number)
    G[a].push([b,1,i])
    G[b].push([a,0,i])
}

const MAX = Number.MAX_VALUE

const dfs = () => {
    const V = Array(N+1).fill(MAX)
    const S = [1]
    let goal = 1
    V[1] = 0

    while (S.length > 0) {
        const n = S.pop()

        for (const [node, f, _] of G[n]) {
            if (V[node] < MAX) continue
            if (f === 0) {
                V[node] = V[n] - 1
            } else {
                V[node] = V[n] + 1
            }
            if(V[goal] > V[node]) {
                goal = node
            }
            S.push(node)
        }
    }
    return goal
}

const dfs2 = (goal) => {
    const edges = Array(N-1).fill('0')

    const S = [goal]
    const V = Array(N+1).fill(0)
    V[goal] = 1

    while (S.length > 0) {
        const n = S.pop()

        for (const [node, f, i] of G[n]) {
            if (V[node] === 1) continue
            V[node] = 1
            if (f === 0) {
                edges[i] = '1'
            }
            S.push(node)
        }
    }

    return edges
}

console.log(dfs2(dfs()).join(''));
