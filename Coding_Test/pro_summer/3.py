def getSp(des, node, check):
    if len(node[des]) == 0:
        check[des] = 1
        return 1
    sp = 0
    for i in node[des]:
        sp += getSp(i, node, check)
    return sp


def solution(total_sp, skills):
    answer = []
    node = [[] for i in range(len(skills)+2)]
    sp = [0 for i in range(len(skills)+2)]
    check = [0 for i in range(len(skills)+2)]
    for i in skills:
        node[i[0]].append(i[1])
    spNum = 0
    for i in range(1, len(node)):
        if len(node[i]) == 0:
            sp[i] = 1
            continue
        for j in node[i]:
            sp[i] += getSp(j, node, check)
    spNum = total_sp//sum(sp)
    answer = list(map(lambda x: x*spNum, sp))[1:]
    return answer
