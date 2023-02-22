import sys


def get_lsp(pattern):
    table = [0 for _ in range(len(pattern))]
    i = 0

    for j in range(1, len(pattern)):

        while i > 0 and pattern[i] != pattern[j]:
            i = table[i-1]

        if pattern[i] == pattern[j]:
            i += 1
            table[j] = i

    return table


# 입력부
pat = sys.stdin.readline().rstrip()

ans = 0
for i in range(len(pat)):
    # 잠재적인 패턴이 될 수 있는 모든 패턴에 대하여 failure 배열을 얻은 후 최대값을 갱신한다
    ans = max(ans, max(get_lsp(pat[i:])))

# 정답 출력
print(ans)
