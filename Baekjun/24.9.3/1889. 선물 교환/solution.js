class Node {
  constructor(value) {
    this.value = value;
    this.prev = null;
    this.next = null;
  }
}
class Deque {
  constructor(init) {
    this.head = null;
    this.tail = null;
    let prev = null;
    if (init) {
      init.forEach((value) => {
        const newNode = new Node();
        newNode.value = value;
        this.tail = newNode;
        if (!this.head) {
          this.head = newNode;
          prev = newNode;
        } else if (prev) {
          prev.next = newNode;
          newNode.prev = prev;
        }
      });
    }
  }

  popleft = () => {
    if (!this.head) return;
    const retValue = this.head.value;
    this.head = this.head.next;
    this.head.prev = null;

    return retValue;
  };

  pop = () => {
    if (!this.tail) return;
    const retValue = this.tail.value;
    this.tail = this.tail.prev;
    this.tail.next = null;
    return retValue;
  };

  append = (value) => {
    const node = new Node(value);
    if (!this.head) this.head = node;
    if (this.tail) {
      this.tail.next = node;
      node.prev = this.tail;
    }
    this.tail = node;
  };

  appendleft = (value) => {
    const node = new Node(value);
    if (!this.tail) this.tail = node;
    if (this.head) {
      this.head.prev = node;
      node.next = this.head;
    }
    this.head = node;
  };

  isEmpty = () => this.head === null;
}

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

const N = Number(input[0]);

const G = Array(N).fill(0);
const indegree = Array(N).fill(0);

for (let i = 0; i < N; i++) {
  let [a, b] = input[i + 1].split(" ").map(Number);
  a -= 1;
  b -= 1;
  G[i] = [a, b];
  indegree[a] += 1;
  indegree[b] += 1;
}

const q = new Deque();
const visited = Array(N).fill(0);

for (let i = 0; i < N; i++) {
  if (indegree[i] < 2) {
    q.append(i);
    visited[i] = 1;
  }
}
while (!q.isEmpty) {
  const node = q.popleft();

  const [a, b] = G[node];

  indegree[a] -= 1;
  indegree[b] -= 1;

  if (indegree[a] < 2 && visited[a] === 0) {
    q.append(a);
    visited[a] = 1;
  }
  if (indegree[b] < 2 && visited[b] === 0) {
    q.append(b);
    visited[b] = 1;
  }
}

const ans = [];

for (let i = 0; i < N; i++) {
  if (visited[i] === 0) {
    ans.push(i + 1);
  }
}

console.log(ans.length);
if (ans.length > 0) {
  console.log(ans.join(" "));
}
