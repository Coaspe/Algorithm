x, y = map(int, input().split())
arr = []
arr2 = set()
s = 0

for i in range(x):
    row = list(map(int, input().split()))
    arr2.add(max(row))
    arr.append(row)
    s += sum(row)

for j in range(y):
    arr2.add(max(arr[i][j] for i in range(x)))

print(s - sum(arr2))
