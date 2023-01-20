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

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word


N, M = map(int, input().split())
trie = Trie()
answer = 0
for _ in range(N):
    trie.insert(input())

for _ in range(M):
    answer += trie.search(input())

print(answer)
