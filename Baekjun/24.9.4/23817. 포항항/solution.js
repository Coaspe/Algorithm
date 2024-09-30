/** @format */

// Use LinkedList to implement Deque
class Deque {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  pushFront(value) {
    const node = { value, next: this.head, prev: null };
    if (this.head) {
      this.head.prev = node;
    } else {
      this.tail = node;
    }
    this.head = node;
    this.size++;
  }

  pushBack(value) {
    const node = { value, next: null, prev: this.tail };
    if (this.tail) {
      this.tail.next = node;
    } else {
      this.head = node;
    }
    this.tail = node;
    this.size++;
  }

  popFront() {
    if (!this.head) return null;
    const value = this.head.value;
    this.head = this.head.next;
    if (this.head) {
      this.head.prev = null;
    } else {
      this.tail = null;
    }
    this.size--;
    return value;
  }

  popBack() {
    if (!this.tail) return null;
    const value = this.tail.value;
    this.tail = this.tail.prev;
    if (this.tail) {
      this.tail.next = null;
    } else {
      this.head = null;
    }
    this.size--;
    return value;
  }

  getFront() {
    return this.head ? this.head.value : null;
  }

  getBack() {
    return this.tail ? this.tail.value : null;
  }

  getSize() {
    return this.size;
  }
}

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

let line = 0;
const [N, M] = input[line++].split(" ").map(Number);
const B = [];

for (let i = 0; i < N; i++) {
  B.push(input[line++].trim().split(""));
}

let start = [0, 0];
for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (B[i][j] === "S") {
      start = [i, j];
    }
  }
}

const find = (r, c) => {
  const visited = Array.from({ length: N }, () => Array(M).fill(false));
  const q = new Deque();
  q.pushBack([r, c, 0]);
  visited[r][c] = true;

  const dist = {};

  while (q.head) {
    const [r, c, d] = q.popFront();

    for (let [dr, dc] of [
      [0, 1],
      [0, -1],
      [1, 0],
      [-1, 0],
    ]) {
      const nr = r + dr;
      const nc = c + dc;

      if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
      if (B[nr][nc] === "X") continue;
      if (visited[nr][nc]) continue;

      visited[nr][nc] = true;
      q.pushBack([nr, nc, d + 1]);
      if (B[nr][nc] === "K") {
        dist[[nr, nc]] = d + 1;
      }
    }
  }

  return dist;
};

const from_start = find(start[0], start[1]);
if (Object.keys(from_start).length < 5) {
  console.log(-1);
  return;
}

const candid = Object.keys(from_start).map((v) => v.split(",").map(Number));
let ans = Infinity;
const dist = [from_start];

for (let i = 0; i < candid.length; i++) {
  const [r, c] = candid[i];
  dist.push(find(r, c));
}

const perm = (arr, selectNum) => {
  let result = [];
  if (selectNum === 1) return arr.map((v) => [v]);
  arr.forEach((v, idx, arr) => {
    const fixer = v;
    const restArr = arr.filter((_, index) => index !== idx);
    const permArr = perm(restArr, selectNum - 1);
    const combineFixer = permArr.map((v) => [fixer, ...v]);
    result.push(...combineFixer);
  });
  return result;
};

const permArr = perm([0, 1, 2, 3, 4], 5);
for (let i = 0; i < permArr.length; i++) {
  const order = permArr[i];
  let sum = 0;
  let prev = 0;
  for (let j = 0; j < order.length; j++) {
    sum += dist[prev][candid[order[j]].join(",")];
    prev = order[j] + 1;
  }
  ans = Math.min(ans, sum);
}

console.log(ans);
