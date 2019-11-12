from collections import Counter
def solution(logs):
    log = logs.split('\n')
    tmp = Counter([(int(i.split()[1].split(':')[0])+9)%24 for i in log])
    answer = [tmp[i] for i in range(24)]
    return answer
