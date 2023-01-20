import collections
from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.word = ''
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: List[str]) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
            node.word = char


level = int(input())
trie = Trie()

for _ in range(level):
    path = input().split()
    n, path = int(path[0]), path[1:]
    trie.insert(path)

queue = collections.deque([(trie.root, -2)])
seen = set()


def dfs(node: TrieNode, dash):
    if node.word:
        print(f"{dash*'-'}{node.word}")

    for noewNode in sorted(node.children.values(), key=lambda x: x.word):
        if noewNode not in seen:
            seen.add(noewNode)
            dfs(noewNode, dash+2)


dfs(trie.root, -2)
