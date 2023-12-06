def solution():
    N = int(input())
    O = list(input().split())
    R = ""

    for a in O:
        if a == "1":
            R += "3"
        elif a == "2":
            R += "4"
        elif a == "3":
            R += "1"
        else:
            R += "2"

    R = R[::-1]
    R += R
    O = "".join(O)
    O += O
    ans = []

    for _ in range(int(input())):
        OO = list(input().split())
        A = "".join(OO)

        if O.find(A) != -1 or R.find(A) != -1:
            ans.append(OO)

    print(len(ans))

    for a in ans:
        print(*a)


if __name__ == "__main__":
    solution()
