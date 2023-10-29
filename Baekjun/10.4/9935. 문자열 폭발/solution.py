# BOJ 9935. 문자열 폭발


def solution(string, bomb):
    stack = []
    for s in string:
        stack.append(s)

        if s == bomb[-1] and "".join(stack[-len(bomb) :]) == bomb:
            del stack[-len(bomb) :]

    return "".join(stack) if stack else "FRULA"


if __name__ == "__main__":
    string = input()
    bomb = input()
    print(solution(string, bomb))
