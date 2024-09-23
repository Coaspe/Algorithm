const fs = require("fs")
const submit = '/dev/stdin'
const dev = './test.txt'
const input = fs.readFileSync(submit).toString().split('\n');

const [N, K] = input[0].split(" ").map((e)=>Number(e))

const A = input[1].split(" ").map((e)=>Number(e))

let l = 0
let r = 1e13

while (r > l + 1) {
    const mid = Math.floor((r + l) / 2)
    let result = 0

    for (let i = 0; i < A.length; i++) {
        const e = A[i];
        result += Math.min(e, mid)
    }

    if (result >= mid * K) {
        l = mid;
    } else {
        r = mid
    }
}

console.log(l);
