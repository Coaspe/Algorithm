import collections


class TrieNode:
    def __init__(self) -> None:
        self.word = False
        self.num = 0
        self.pnode: TrieNode = None
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node.children[char].pnode = node
            node = node.children[char]
        node.word = True


def count(node: TrieNode):
    node.num = node.pnode.num + \
        (node.pnode == trie.root or node.pnode.word or len(node.pnode.children) > 1)
    if node.word:
        global ans
        ans += node.num
    for val in node.children.values():
        count(val)


while 1:
    ans = 0
    trie = Trie()
    try:
        N = int(input())
    except:
        break

    for _ in range(N):
        trie.insert(input())

    for val in trie.root.children.values():
        val.pnode = trie.root
        count(val)

    print("%.2f" % (ans/N))
