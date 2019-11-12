from math import ceil
def solution(s):
    ans = 0
    li = [0 for i in range(0,5)]
    for i in s:
        li[i] += 1
    print(li)
    for i in range(len(li)-1,0,-1):
        if i == 4:
            ans += li[i]
        elif i == 3:
            tmp = min(li[3],li[1])
            li[3] -= tmp
            li[1] -= tmp
            ans += tmp
            ans += li[3]
        elif i == 2:
            tmp = ceil(li[2]/2)
            ans += tmp
        elif i == 1:
            ans += ceil(li[1]/4)
    print(ans)
    return ans
