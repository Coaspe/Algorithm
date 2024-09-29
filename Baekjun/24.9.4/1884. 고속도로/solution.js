
class Heapq {
  constructor() {
    this.heap = [];
    this.compare = (a, b) => {
      for (let i = 0; i < a.length; i++) {
        if (a[i] < b[i]) return -1;
        if (a[i] > b[i]) return 1;
      }
      return 0;
    };
    this.heappush = (value) => {
      this.heap.push([...value]);
      this.heapUp();
    };
    this.getLeftChildIndex = (parentIndex) => parentIndex * 2 + 1;
    this.getRightChildIndex = (parentIndex) => parentIndex * 2 + 2;
    this.getParentIndex = (childIndex) => Math.floor((childIndex - 1) / 2);
    this.heapUp = () => {
      let index = this.heap.length - 1;
      let lastNode = [...this.heap[index]];
      while (index > 0) {
        const parent = this.getParentIndex(index);
        if (this.compare(this.heap[parent], lastNode) === 1) {
          this.heap[index] = [...this.heap[parent]];
          index = parent;
        } else {
          break;
        }
      }
      this.heap[index] = lastNode;
    };
    this.heapDownFrom = (index) => {
      const count = this.heap.length;
      const rootNode = [...this.heap[index]];
      while (this.getLeftChildIndex(index) < count) {
        const leftChild = this.getLeftChildIndex(index);
        const rightChlid = this.getRightChildIndex(index);
        const smallerChild = rightChlid < count && this.compare(this.heap[rightChlid], this.heap[leftChild]) === -1 ? rightChlid : leftChild;
        if (this.compare(this.heap[smallerChild], rootNode) <= 0) {
          this.heap[index] = [...this.heap[smallerChild]];
          index = smallerChild;
        } else {
          break;
        }
      }
      this.heap[index] = rootNode;
    };
    this.heappop = () => {
      const count = this.heap.length;
      const rootNode = [...this.heap[0]];
      if (count <= 0) return undefined;
      if (count === 1) this.heap = [];
      else {
        this.heap[0] = [...this.heap.pop()];
        this.heapDownFrom(0);
      }
      return rootNode;
    };
  }
}

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");
let line = 0

const K = Number(input[line++])
const N = Number(input[line++])
const R = Number(input[line++])

const G = Array.from(Array(N), ()=>[])

for (let i = 0; i < R; i++) {
    const [s, d, l, t] = input[line++].split(" ").map(Number)
    G[s - 1].push([d - 1, l, t])
}

const MAX = Number.MAX_VALUE

const dp = Array.from(Array(N), () => Array(K + 1).fill(MAX))
dp[0][K] = 0

const hq = new Heapq()
hq.heappush([0, K, 0])

answer = MAX

while (hq.heap.length > 0) {
    const [dist, cost, node] = hq.heappop()

    if (node === N - 1) {
        answer = Math.min(answer, dist)
        break;
    }

    for (const [next_node, next_dist, next_cost] of G[node]) {
        const new_dist = next_dist + dist
        const new_cost = cost - next_cost

        if (new_cost >= 0 && dp[next_node][new_cost] > new_dist) {
            dp[next_node][new_cost] = new_dist
            hq.heappush([new_dist, new_cost, next_node])
        }
    }
}

console.log(answer === MAX ? -1 : answer);
