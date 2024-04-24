from itertools import combinations

N = int(input())
result = []
R = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

for i in range(1, 11):
    for j in combinations(R, i):
        num = "".join(list(reversed(j)))
        result.append(int(num))

result.sort()
if N >= len(result):
    print(-1)
else:
    print(result[N])
