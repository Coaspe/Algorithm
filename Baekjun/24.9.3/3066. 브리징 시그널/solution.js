/** @format */

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

let T = Number(input[0]);
let line = 0;

const bisect_left = (n, arr) => {
  let [l, r] = [-1, arr.length];
  while (r > l + 1) {
    const mid = Math.floor((l + r) / 2);

    if (arr[mid] >= n) {
      r = mid;
    } else {
      l = mid;
    }
  }
  return r;
};

while (T) {
  let dp = [];
  T -= 1;

  const N = Number(input[++line]);
  for (let i = 0; i < N; i++) {
    const n = Number(input[++line]);
    const idx = bisect_left(n, dp);

    if (idx === dp.length) {
      dp.push(n);
    } else {
      dp[idx] = n;
    }
  }
  console.log(dp.length);
}
