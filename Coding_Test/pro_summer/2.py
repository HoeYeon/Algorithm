
def getPower(n):
    power = 1
    count = 0
    while power < n:
        power *= 2
        count += 1
    return count if power == n else count-1


def solution(n):
    answer = 0
    while n != 0:
        power = getPower(n)
        answer += 3**power
        n = n - 2**power
    return answer
