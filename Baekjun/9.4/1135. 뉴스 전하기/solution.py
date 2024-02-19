n = int(input())
emp = list(map(int, input().split()))
node = [[] for _ in range(n)]
child_cnt = [0 for _ in range(n)]


def go(x):
    global child_cnt
    child_node = []

    if len(node[x]) == 0:
        child_cnt[x] = 0
        return

    for child in node[x]:
        go(child)
        child_node.append(child_cnt[child])

    child_node.sort(reverse=True)
    child_node = [child_node[i] + i + 1 for i in range(len(child_node))]
    child_cnt[x] = max(child_node)


for i in range(1, len(emp)):
    node[emp[i]].append(i)

go(0)
print(child_cnt[0])
