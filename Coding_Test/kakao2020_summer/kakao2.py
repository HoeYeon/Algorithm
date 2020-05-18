from itertools import permutations


def split_expression(expression, op):
    e = []
    ops = []
    tmp = ''
    for i in expression:
        if i in op:
            e.append(0 if tmp == '0' else int(tmp))
            e.append(i)
            tmp = ''
            ops.append(i)
        else:
            tmp += i
    e.append(int(tmp))
    return e, list(set(ops))


def calculate(sublist):
    if sublist[1] == '+':
        return [sublist[0] + sublist[2]]
    elif sublist[1] == '-':
        return [sublist[0]-sublist[2]]
    else:
        return [sublist[0] * sublist[2]]


def solution(expression):
    answer = 0
    expression, ops = split_expression(expression, ['+', '*', '-'])
    priors = list(map(list, permutations(ops)))
    for prior in priors:
        tmp = expression[:]
        for op in prior:
            while op in tmp:
                for i, v in enumerate(tmp):
                    if v == op:
                        tmp[i-1:i+2] = calculate(tmp[i-1:i+2])
                        break
        answer = max(answer, abs(tmp[0]))
    return answer
