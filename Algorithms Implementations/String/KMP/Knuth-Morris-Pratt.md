# Knuth-Morris-Pratt

## Pseudo code

```
algorithm kmp_search:
    input:
        검색 될 텍스트, S (the text to be searched)
        찾아야하는 단어, W (the word sought)
    output:
        W가 S 안에서 발견 됐을 때의 위치, P
        발견된 단어의 개수, nP

    define variables:
        S 안에서 현재 위치, j ← 0
        W 안에서 현재 위치, k ← 0
        다른 곳에서 계산되는 테이블, T

    let nP ← 0

    while j < length(S) do
        # 검색 될 텍스트와 찾아야하는 단어의 현재 위치에 해당하는 문자가 같다면,
        if W[k] = S[j] then
            # 각각 인덱스 증가
            let j ← j + 1
            let k ← k + 1

            if k = length(W) then
                (단어 발견, 단어 한 개만 찾는다면, m ← j - k 를 반환하면 됩니다.)
                let P[nP] ← j - k, nP ← nP + 1
                let k ← T[k] (T[length(W)] can't be -1)
        else
            let k ← T[k]
            if k < 0 then
                let j ← j + 1
                let k ← k + 1
```

## "Partial match" 테이블

이 테이블은 `S`에 있는 문자들이 두 번 이상 매치를 실행하지 않기 위해 존재합니다.
이를 가능하게 하는 선형 검색의 특성에 대한 핵심은 패턴의 _초기 세그먼트_ 에 대해 주 문자열의 일부 세그먼트를 확인함으로써 현재 위치 이전에 현재 위치로 계속될 수 있는 새로운 잠재적 일치가 어느 위치에서 시작될 수 있는지 정확히 알고 있다는 것입니다. 다시 말해, 패턴 자체를 "사전 검색" 하고, 그렇게 함으로써 잠재적인 일치를 놓치지
않으면서 가망이 없는 문자들을 우회하는 가능한 모든 폴백 위치의 목록을 컴파일합니다.