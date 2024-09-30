/** @format */

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

let line = 0;
let N = Number(input[line++]);

const ps = [];
const psu = [];

for (let i = 0; i < N; i++) {
  const [a, b] = input[line++].split(" ").map(Number);
  ps.push([a, b, a + b]);
  psu.push([a, b, a - b]);
}

ps.sort((a, b) => a[2] - b[2]);
psu.sort((a, b) => a[2] - b[2]);

console.log(Math.max(Math.abs(ps[0][0] - ps[N - 1][0]) + Math.abs(ps[0][1] - ps[N - 1][1]), Math.abs(psu[0][0] - psu[N - 1][0]) + Math.abs(psu[0][1] - psu[N - 1][1])));
