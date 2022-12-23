def countTexts(_, K):
    m = [1]
    for p, k in zip('.' + K, K):

        print(m, m[:-(k != p or 3 + (k in '79'))])
        del m[:-(k != p or 3 + (k in '79'))]
        m += sum(m) % 1000000007,
    return m[-1]
