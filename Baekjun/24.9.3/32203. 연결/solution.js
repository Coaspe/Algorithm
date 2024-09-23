const fs = require("fs")
const submit = '/dev/stdin'
const dev = './test.txt'
const input = fs.readFileSync(submit).toString().split('\n');

const [N, M] = input[0].split(' ').map(Number);
const C = input[1].split(' ').map(Number);

let P = C.map((val, i) => [i, val % 2, val % 2 === 0 ? 1 : 0]);

function find(c) {
    if (P[c][0] !== c) {
        P[c][0] = find(P[c][0]);
    }
    return P[c][0];
}

function union(c1, c2) {
    const p1 = find(c1);
    const p2 = find(c2);

    if (p1 === p2) {
        return [-1, -1, -1];
    }

    if (p1 > p2) {
        P[p1] = [p1, P[p1][1] + P[p2][1], P[p1][2] + P[p2][2]];
        P[p2] = [p1, 0, 0];
        return [p2, p1, (P[p1][1] + P[p2][1]) * (P[p1][2] + P[p2][2])];
    } else {
        P[p2] = [p2, P[p1][1] + P[p2][1], P[p1][2] + P[p2][2]];
        P[p1] = [p2, 0, 0];
        return [p1, p2, (P[p1][1] + P[p2][1]) * (P[p1][2] + P[p2][2])];
    }
}

let dic = {};
let ans = 0;

for (let i = 2; i < 2 + M; i++) {
    let [a, b] = input[i].split(' ').map(Number);
    a -= 1;
    b -= 1;

    let [r, np, v] = union(a, b);

    if (r === -1) {
        console.log(ans);
        continue;
    }

    if (dic[r] === undefined) dic[r] = 0;

    ans -= dic[r];
    dic[r] = 0;

    if (dic[np] === undefined) dic[np] = 0;

    ans += v - dic[np];
    dic[np] = v;

    console.log(ans);
}