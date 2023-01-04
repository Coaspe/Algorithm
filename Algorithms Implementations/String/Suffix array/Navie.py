s = input()
arr = []
for i in range(len(s)):
    arr.append(s[-(i+1):])
arr.sort()
for s in arr:
    print(s)

"""
Time: O(n^2logn)
"""