/** @format */

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

let line = 0;
let N = Number(input[line++]);

const dict = {};

for (let i = 0; i < N; i++) {
  const s = input[line++].split("\\");
  let cur = dict;
  for (let j = 0; j < s.length; j++) {
    let folder = s[j];
    if (folder.length >= 2 && folder[folder.length - 2] == "\\" && folder[folder.length - 1] == "r") {
      folder = folder.slice(0, folder.length - 2);
    }
    if (!(folder in cur)) {
      cur[folder] = {};
    }
    cur = cur[folder];
  }
}

const dfs = (depth, cur) => {
  Object.keys(cur)
    .sort()
    .forEach((key) => {
      console.log(key.padStart(depth + key.length, " "));
      dfs(depth + 1, cur[key]);
    });
};

dfs(0, dict);
