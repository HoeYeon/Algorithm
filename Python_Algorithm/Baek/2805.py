from collections import Counter
N,M = map(int,input().split())
li = list(map(int,input().split()))
c = Counter(li)
li = sorted(list(set(li)),reverse=True)
left = li[0] - M if li[0] > M else 0
right = li[0]
result = 0
while left <= right:
    mid = (left+right)//2
    cnt = 0
    for i in li:
        if i<=mid:
            break
        cnt += (i-mid)*c[i]
    if cnt >= M:
        left = mid+1
        result = mid
    else:
        right = mid-1
print(result)