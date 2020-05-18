def solution(gems):
    answer = []
    min_sec = 999999
    start = 0
    category = set(gems)
    cate_length = len(category)
    check = False
    d = dict.fromkeys(category, 0)
    for end, v in enumerate(gems):
        d[v] += 1
        if end >= cate_length-1 and not check:
            for value in d.values():
                if value == 0:
                    check = False
                    break
                check = True
        if check:
            while d[gems[start]] > 1:
                d[gems[start]] -= 1
                start += 1
            if end-start < min_sec:
                answer = [start+1, end+1]
                min_sec = end-start

    return answer
