import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)
N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

nodeNum = [0]*(N+1)
for i in range(N):
    nodeNum[inorder[i]] = i


def preorder(inStart, inEnd, postStart, postEnd):
    if inStart > inEnd or postStart > postEnd:
        return

    root = postorder[postEnd]

    leftNode = nodeNum[root] - inStart
    rightNode = inEnd - nodeNum[root]

    print(root, end=" ")

    preorder(inStart, nodeNum[root] - 1, postStart, postStart + leftNode - 1)
    preorder(nodeNum[root]+1, inEnd, postEnd - rightNode, postEnd-1)


preorder(0, N-1, 0, N-1)
