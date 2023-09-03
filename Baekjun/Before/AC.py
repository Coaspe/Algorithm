from collections import deque
T = int(input())


def processing(st: str):
    st = st[1:-1]
    return deque(st.split(','))


while T:
    T -= 1
    FB = True

    op = input()
    n = int(input())
    arr = processing(input())

    R = D = 0

    for o in op:
        if o == 'R':
            R += 1
        else:
            D += 1

    if D > n:
        print('error')
        continue

    for s in op:
        if s == 'R':
            FB = not FB
        else:
            if FB:
                arr.popleft()
            else:
                arr.pop()

    arr = list(arr)

    if R % 2:
        arr.reverse()

    ans = ','.join(arr)
    print(f'[{ans}]')
