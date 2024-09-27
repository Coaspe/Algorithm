/** @format */

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

let line = 0;
let N = Number(input[line++]);

let [l, r] = [0, Math.floor(N / 2)];
const A = [];
for (let i = 0; i < N; i++) {
  A.push(Number(input[line++]));
}

A.sort();
let ans = 0;

while (r < N && l < Math.floor(N / 2)) {
  if (A[r] / A[l] >= 2) {
    ans += 1;
    l += 1;
  }
  r += 1;
}

console.log(N - ans);
