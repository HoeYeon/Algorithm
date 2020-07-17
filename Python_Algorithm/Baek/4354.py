def getPI(pattern):
    patternLength = len(pattern)
    pi = [0 for i in range(patternLength)]
    begin = 1
    m = 0
    while begin + m < patternLength:
        if pattern[begin + m] == pattern[m]:
            m += 1
            pi[begin + m - 1] = m
        else:
            if m == 0:
                begin += 1
            else:
                begin += m - pi[m - 1]
                m = pi[m - 1]
    return pi


ans = ""
while True:
    s = input()
    if s == ".":
        break
    pi = getPI(s)
    # 마지막에 반복되는 문자열 제곱수가 부분으로 있을때 처리
    # ex) abcabcab --> 실패함수는 값을 가지고 있지만 1이 되어야함
    if pi[len(s) - 1] % (len(s) - pi[len(s) - 1]):
        ans += "1\n"
    else:
        ans += str(len(s) // (len(s) - pi[len(s) - 1])) + "\n"

print(ans)
