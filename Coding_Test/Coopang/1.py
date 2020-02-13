def solution(n, min_position,max_position, positions):
    answer = []
    positions = sorted(positions)
    thr = (max_position - min_position)//(n-1)
    house = [i for i in range(min_position, max_position+1,thr)]
    result = sorted(list(set(house) - set(positions)))
    return result