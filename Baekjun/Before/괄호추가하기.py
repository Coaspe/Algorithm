def cal2(lst):
    op, num = [], []
    for i in lst[::-1]:
        if i == '+' or i == '-' or i == '*':
            op.append(i)
        else:
            num.append(int(i))
    while len(num) > 1:
        n1 = num.pop()
        n2 = num.pop()
        oper = op.pop()
        if oper == '+':
            num.append(n1 + n2)
        elif oper == '-':
            num.append(n1 - n2)
        elif oper == '*':
            num.append(n1 * n2)
    return num.pop()


def cal(cal_s):
    lst = []
    i = 0
    while i < len(cal_s):
        if cal_s[i] == '(':
            temp = str(cal_s[i+1]) + str(cal_s[i+3]) + str(cal_s[i+5])
            lst.append(str(eval(temp)))
            i += 7
            continue
        elif cal_s[i] != '#' and cal_s[i] != ')':
            lst.append(cal_s[i])
        i += 1
    return cal2(lst)


def sol(idx):
    global result
    for i in range(idx, len(S), 4):
        if i+6 >= len(S):
            continue
        S[i] = '('
        S[i+6] = ')'
        result = max(result, cal(S))
        sol(i+8)
        S[i] = '#'
        S[i+6] = '#'
    return result


N = int(input())
S = '#'
for i in input():
    S += i+'#'
S = list(S)
result = cal(S)
print(sol(0))
