from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
A.reverse()
dic = defaultdict(int)

while A:
    a = A.pop()
    dic[a - 1] += 1
    if dic[a]:
        dic[a] -= 1
print(sum(dic.values()))
