n = int(input())
val = [*str(n)[::-1]]
new_val = ['9' for _ in range(len(val)-1)] + [val[-1]]
arr = []
for i in range(10):
    arr.append([10**i, i * int(10**(i-1))])
ans = [0] * 10
for i in range(len(new_val)):
    for j in range(int(new_val[i])):
        if i != 0:
            ans[j+1] += (int(new_val[i-1])+1) * 10 ** (i-1)
            for k in range(10):
                ans[k] += max(1, i * 10 ** (i-1))
        else:
            ans[j+1] += 1
for i in range(len(val)-2, -1, -1):
    for j in range(9, int(val[i]), -1):
        ans[j] -= arr[i][0]
        for k in range(len(val)-1, i, -1):
            ans[int(val[k])] -= arr[i][0]
        for k in range(10):
            ans[k] -= arr[i][1]
print(*ans)
