def solution(words):
    d = {}
    ans = []
    for i, v in enumerate(words):
        if v not in d:
            d[v] = i+1
        ans.append(d[v])

    return ans
