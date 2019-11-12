def solution(forms):
    answer = []
    name = [i[1] for i in forms]
    dd = {}
    for i in forms:
        dd[i[1]] = i[0]
    comb = []
    for i in name:
        tmp = [i[j:j+2] for j in range(len(i)-1)]
        comb.append(tmp)
    check2 = [0 for i in range(len(name))]
    for i in range(len(name)):
        if check2[i] == 1:
            continue
        for k in range(i+1,len(name)):
            for j in comb[i]:
                if j in comb[k]:
                    answer.append(dd[name[i]])
                    answer.append(dd[name[k]])
                    check2[i] = 1
                    check2[k] = 1
    answer = sorted(list(set(answer)))
    return answer
