n = int(input())
e = float('-inf')
arr = []
answer = 0

for _ in range(n):
    arr.append(tuple(map(int, input().split())))

arr.sort(key=lambda x: (x[1],  x[0]))

for i in range(len(arr)):
    s, end = arr[i]
    if s >= e:
        e = end
        answer += 1

print(answer)
