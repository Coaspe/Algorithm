import bisect


dic = {}
lst = []
lis = [-1]
result = []
backtrace = []
n = int(input())

for i in range(n):
    a, b = map(int, input().split(' '))
    dic[b] = a

temp = sorted(dic)

for i in temp:
    lst.append(dic.get(i))

for i in lst:
    if i > lis[-1]:
        lis.append(i)
    else:
        lis[bisect.bisect_left(lis, i)] = i

    result.append(lis.index(i)+1)

lisLength = len(lis)

for i in range(len(lst)-1, -1, -1):
    if result[i] == lisLength:
        backtrace.append(lst[i])
        lisLength -= 1

print(n - (len(lis) - 1))

lst.sort()

for i in backtrace:
    lst.remove(i)
for i in lst:
    print(i)
