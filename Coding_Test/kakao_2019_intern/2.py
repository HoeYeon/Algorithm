from collections import Counter
def solution(s):
    answer = []
    s = s[1:-1]
    tmp = []
    num = []
    ss = ''
    check = False
    for i in s:
        if i == '{':
            check = True
            continue
        if i == '}':
            tmp.append(ss)
            num.extend(tmp)
            tmp = []
            ss = ''
            check = False
            continue
        if i == ',':
            if check:
                tmp.append(ss)
                ss = ''
        else:
            ss += i
    num = Counter(num)
    answer = [int(i[0]) for i in num.most_common(len(num))]

    return answer
