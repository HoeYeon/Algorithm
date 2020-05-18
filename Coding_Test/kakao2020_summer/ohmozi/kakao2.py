import re
from itertools import permutations


def solution(expression):
    operation = ['*', '+', '-']
    operation_permu = list(permutations(operation, 3))
    print(operation_permu)

    result_list = []

    # numbers = numbers1.copy()
    # opers = opers1.copy()

    # expression_list = []
    # for i in range(len(opers1)):
    #     expression_list.append(numbers1[i])
    #     expression_list.append(opers1[i])
    # expression_list.append(numbers1[-1])
    # print(expression_list)

    numbers_temp = []
    opers_temp = []
    for i in range(len(operation_permu)):
        numbers1 = re.findall("\d+", expression)
        opers1 = re.findall("\D+", expression)

        print("------oper 조합: ", operation_permu[i])
        print("numbers1: ", numbers1, "opers1: ", opers1)
        numbers = numbers1
        opers = opers1
        for oper in operation_permu[i]:

            for i in range(len(opers)):
                op = opers.pop()
                print(oper)
                if op != oper:
                    opers_temp.append(op)
                    numbers_temp.append(numbers.pop())
                    print("numbers:", numbers)
                    print("opers:", opers)
                elif op == oper:
                    if op == "*":
                        v1 = numbers.pop()
                        v2 = numbers.pop()
                        result = int(v1) * int(v2)
                        numbers.append(result)
                    elif op == "+":
                        v1 = numbers.pop()
