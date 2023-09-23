(_, MAX_LINES) = map(int, input().split())
L = list(map(int, input().split()))


def check_width(W, L, MAX_LINES):
    lines = 1
    remaining_width = W

    for word_width in L:
        if word_width < W:
            return False
        # After the first word, we need to account for the space
        if remaining_width < W:
            remaining_width -= 1

        # If the word is too long to fit on a line, go to the next line
        if remaining_width < word_width:
            lines += 1
            remaining_width = W

        remaining_width -= word_width

    return lines <= MAX_LINES


def min_window_width(L, MAX_LINES):
    low, high = max(L), sum(L) + (len(L) - 1)

    while low + 1 < high:
        mid = (low + high) // 2
        if check_width(mid, L, MAX_LINES):
            high = mid
        else:
            low = mid

    return high


print(min_window_width(L, MAX_LINES))
