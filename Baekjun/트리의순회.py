import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)
N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

nodeNum = [0]*(N+1)
for i in range(N):
    nodeNum[inorder[i]] = i


def preoder(inStart, inEnd, postStart, postEnd):
    if inStart > inEnd or postStart > postEnd:
        return

    root = postorder[postEnd]

    leftNode = nodeNum[root] - inStart
    rightNode = inEnd - nodeNum[root]

    print(root, end=" ")

    preoder(inStart, nodeNum[root] - 1, postStart, postStart + leftNode - 1)
    preoder(nodeNum[root]+1, inEnd, postEnd - rightNode, postEnd-1)


preoder(0, N-1, 0, N-1)
