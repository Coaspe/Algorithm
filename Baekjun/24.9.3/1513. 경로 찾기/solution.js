/** @format */

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let [N, M, C] = input[0].split(" ").map((e) => Number(e));

let B = Array.from(Array(N + 1), () => Array(M + 1).fill(0));

const MOD = 1_000_007;

let dp = Array.from(Array(N + 1), () => Array.from(Array(M + 1), () => Array.from(Array(C + 1), () => Array(C + 1).fill(0))));
dp[1][1][0][0] = 1;

for (let i = 1; i < input.length; i++) {
  const element = input[i];
  let [r, c] = element.split(" ").map((e) => Number(e));

  B[r][c] = i;

  if (r === 1 && c === 1) {
    dp[1][1][0][0] = 0;
    dp[1][1][i][1] = 1;
  }
}

for (let i = 1; i < N + 1; i++) {
  for (let j = 1; j < M + 1; j++) {
    if (i === 1 && j === 1) continue;

    if (B[i][j] !== 0) {
      for (let c = 0; c < B[i][j]; c++) {
        for (let n = 0; n < c + 1; n++) {
          dp[i][j][B[i][j]][n + 1] += dp[i - 1][j][c][n] + dp[i][j - 1][c][n];
          dp[i][j][B[i][j]][n + 1] %= MOD;
        }
      }
    } else {
      for (let c = 0; c < C + 1; c++) {
        for (let n = 0; n < c + 1; n++) {
          dp[i][j][c][n] += dp[i - 1][j][c][n] + dp[i][j - 1][c][n];
          dp[i][j][c][n] %= MOD;
        }
      }
    }
  }
}

let ans = "";

for (let i = 0; i < C + 1; i++) {
  let element = 0;
  for (let j = 0; j < C + 1; j++) {
    element += dp[N][M][j][i];
    element %= MOD;
  }
  ans += String(element);
  ans += " ";
}

console.log(ans);
