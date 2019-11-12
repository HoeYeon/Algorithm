'''def solution(stones, k):
    answer = 0
    check = True
    num = 0
    j=0
    while check:
        j += 1
        s = [i-j for i in stones]
        count = 0
        for i in s:
            if i <= 0:
                count += 1
            else:
                count = 0
            if count == k:
                check = False
                break
        num +=1
    answer = num
    return answer'''

def solution(stones, k):
    ans = 2000000001
    i = 0
    while i<len(stones):
        tmp = max(stones[i:i+k])
        if i+k > len(stones):
            break
        if tmp < ans:
            #i =stones.index(min(stones[i:i+k]))
            ans = tmp
            #print(tmp)
            i+=1
        else:
            i += 1
    return ans
