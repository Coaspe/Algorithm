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

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


class Node:
    def __init__(self) -> None:
        self.children = collections.defaultdict(Node)
        self.word = False


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def insert(self, word):
        root = self.root
        for w in word:
            root = root.children[w]
        root.word = True
