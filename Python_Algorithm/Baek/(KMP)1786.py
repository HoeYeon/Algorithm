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


def KMP(text, pattern):
    textLength = len(text)
    patternLength = len(pattern)
    ans = []
    textIdx = 0
    patternIdx = 0
    pi = getPI(pattern)
    while textIdx <= textLength - patternLength:
        if (
            patternIdx < patternLength
            and text[textIdx + patternIdx] == pattern[patternIdx]
        ):
            patternIdx += 1
            if patternIdx == patternLength:
                ans.append(str(textIdx + 1))
        else:
            if patternIdx == 0:
                textIdx += 1
            else:
                textIdx += patternIdx - pi[patternIdx - 1]
                patternIdx = pi[patternIdx - 1]

    return ans


T = input()
P = input()
ans = KMP(T, P)
print(len(ans))
print(" ".join(ans))

