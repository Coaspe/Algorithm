import sys


def back_tracking(cnt, idx):

    # 암호를 만들었을 때
    if cnt == l:
        # 모음, 자음 체크
        vo, co = 0, 0

        for i in range(l):
            if answer[i] in consonant:
                vo += 1
            else:
                co += 1

        # 모음 1개 이상, 자음 2개 이상
        if vo >= 1 and co >= 2:
            print("".join(answer))

        return

    # 반복문을 통해 암호를 만든다.
    for i in range(idx, c):
        answer.append(words[i])
        back_tracking(cnt + 1, i + 1)  # 백트래킹
        answer.pop()


l, c = map(int, sys.stdin.readline().split())
words = sorted(list(map(str, sys.stdin.readline().split())))
consonant = ['a', 'e', 'i', 'o', 'u']
answer = []
back_tracking(0, 0)
