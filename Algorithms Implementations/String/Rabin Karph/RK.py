def RabinKarp(s, pattern):
    pattern_hash = hash(pattern)  # 1. 패턴의 hash값을 구한다
    n = len(pattern)

    for i in range(len(s)):
        s_hash = hash(s[i:i+n])     # 2. 문자열의 패턴의 길이만큼 hash값을 구한다.
        if pattern_hash == s_hash:  # 2-2 : 해쉬값이 일치하다면
            if pattern == s[i:i+n]:  # 2-2-1 : 패턴과 문자열이 일치한지 확인
                return i

    return -1
