import collections


class TrieNode:
    def __init__(self) -> None:
        self.children = collections.defaultdict(
            lambda: TrieNode()
        )  # lambda를 사용하여 안전한 생성
        self.count = 0  # 현재 노드에서 끝나는 단어 개수를 저장


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.count += 1  # 단어의 끝을 표시


def solution(words):
    if not words:
        return 0

    answer = 0
    T = Trie()

    for word in words:
        T.insert(word)

    def count_words(node):
        total = node.count  # 현재 노드가 단어의 끝이면 해당 개수를 저장

        for child in node.children.values():
            total += count_words(child)

        return total

    count_words(T.root)

    for word in words:
        node = T.root
        typed = 0

        for char in word:
            node = node.children[char]
            typed += 1

            if node.count > 0:  # 단어의 끝에 도달하면 입력 중지
                break

        answer += typed

    return answer
