class Heap {
  constructor() {
    this.heap = [];
  }

  getLeftChildIndex = (parentIndex) => parentIndex * 2 + 1;
  getRightChildIndex = (parentIndex) => parentIndex * 2 + 2;
  getParentIndex = (childIndex) => Math.floor((childIndex - 1) / 2);

  compare = (a, b) => {
    for (let i = 0; i < a.length; i++) {
      if (a[i] < b[i]) return -1;
      if (a[i] > b[i]) return 1;
    }
    return 0;
  };

  peek = () => this.heap[0];

  insert = (value) => {
    this.heap.push([...value]);
    this.heapifyUp();
  };

  heapifyUp = () => {
    let index = this.heap.length - 1;
    const lastInsertedNode = [...this.heap[index]];

    while (index > 0) {
      const parentIndex = this.getParentIndex(index);

      if (this.compare(this.heap[parentIndex], lastInsertedNode) > 0) {
        this.heap[index] = [...this.heap[parentIndex]];
        index = parentIndex;
      } else break;
    }

    this.heap[index] = lastInsertedNode;
  };

  remove = () => {
    const count = this.heap.length;
    const rootNode = [...this.heap[0]];

    if (count <= 0) return undefined;
    if (count === 1) this.heap = [];
    else {
      this.heap[0] = [...this.heap.pop()];
      this.heapifyDownFrom(0);
    }

    return rootNode;
  };

  heapify = (arr) => {
    this.heap = arr.map((item) => [...item]);
    const lastParentIndex = this.getParentIndex(this.heap.length - 1);

    for (let i = lastParentIndex; i >= 0; i--) {
      this.heapifyDownFrom(i);
    }
  };

  heapifyDownFrom = (index) => {
    const count = this.heap.length;
    const rootNode = [...this.heap[index]];

    while (this.getLeftChildIndex(index) < count) {
      const leftChildIndex = this.getLeftChildIndex(index);
      const rightChildIndex = this.getRightChildIndex(index);

      const smallerChildIndex = rightChildIndex < count && this.compare(this.heap[rightChildIndex], this.heap[leftChildIndex]) < 0 ? rightChildIndex : leftChildIndex;

      if (this.compare(this.heap[smallerChildIndex], rootNode) <= 0) {
        this.heap[index] = [...this.heap[smallerChildIndex]];
        index = smallerChildIndex;
      } else break;
    }

    this.heap[index] = rootNode;
  };
}

class PQ extends Heap {
  constructor() {
    super();
  }

  heappush = (value) => this.insert(value);
  heappop = () => this.remove();
}

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

const N = Number(input[0]);
const S = input[1].split("").map((e, i) => [e, -i]);
const S2 = S.map((e) => [e[0], -e[1]]);
const hq = new PQ();

let da = "";
let ne = S.pop()[0];
S2.pop();

hq.heapify(S);
const removed = Array(N).fill(0);

while (hq.heap.length > 0) {
  let [v, i] = hq.heappop();

  i = -i;

  if (removed[i]) continue;

  removed[i] = 1;
  da += v;

  while (S2.length > 0 && removed[S2[S2.length - 1][1]]) {
    S2.pop();
  }

  if (S2.length > 0) {
    const [vv, ii] = S2.pop();
    removed[ii] = 1;
    ne += vv;
  }
}

console.log(da < ne ? "DA" : "NE");
console.log(da);
