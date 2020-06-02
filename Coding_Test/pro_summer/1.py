from collections import Counter


def solution(p):
    for i in range(p+1, 10001):
        if all([v == 1 for v in Counter(list(str(i))).values()]):
            return i
