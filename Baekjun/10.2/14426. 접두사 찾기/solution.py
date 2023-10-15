import sys

input = sys.stdin.readline
N, M = map(int, input().split())
S = [input().rstrip() for _ in range(N)]
L = [input().rstrip() for _ in range(M)]

import collections


class TrieNode:
    def __init__(self) -> None:
        self.word = False
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


T = Trie()
for s in S:
    T.insert(s)
ans = 0
for l in L:
    ans += T.startsWith(l)
print(ans)
