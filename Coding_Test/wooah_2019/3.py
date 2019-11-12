def solution(prices, discounts):
    p = sorted(prices, reverse=True)
    d = sorted(discounts, reverse=True)
    if len(p) <= len(d):
        l = len(p)
        n_p = d[l:]
    else:
        l = len(d)
        n_p = p[l:]
    for i in range(l):
        n_p.append(p[i]*(100-d[i])//100)
    answer = sum(n_p)
    return answer
