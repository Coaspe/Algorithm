/** @format */

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

const [N, M, D, E] = input[0].split(" ").map(Number);
const H = input[1].split(" ").map(Number);

const G = Array.from(Array(N), () => Array());

const MIN = -2e14;

for (let i = 0; i < M; i++) {
  let [a, b, c] = input[i + 2].split(" ").map(Number);
  a -= 1;
  b -= 1;
  G[a].push([b, c]);
  G[b].push([a, c]);
}
const CU = Array(N).fill(MIN);
const CD = Array(N).fill(MIN);

const q = new Heapq();

q.heappush([0, 0, 0, 0]);

while (q.heap.length > 0) {
  let [value, total_d, node, ud] = q.heappop();

  value = -value;
  if ((ud === 0 && CU[node] > value) || (ud === 1 && CD[node] > value)) {
    continue;
  }

  for (let i = 0; i < G[node].length; i++) {
    let [next_node, next_cost] = G[node][i];
    new_d = total_d + next_cost;
    new_value_u = H[next_node] * E - new_d * D;
    new_value_d = value - next_cost * D;

    if (H[next_node] > H[node] && ud === 0 && new_value_u > CU[next_node]) {
      CU[next_node] = new_value_u;
      q.heappush([-new_value_u, new_d, next_node, 0]);
    } else if (H[next_node] < H[node] && new_value_d > CD[next_node]) {
      CD[next_node] = new_value_d;
      q.heappush([-new_value_d, new_d, next_node, 1]);
    }
  }
}

console.log(CD[N - 1] > MIN ? CD[N - 1] : "Impossible");
