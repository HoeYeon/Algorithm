import sys

input = sys.stdin.readline

N,M = map(int,input().split())
li = sorted([int(input()) for i in range(N)])

left = 1
right = li[-1] - li[0]
result = 0
while left <= right:
    mid = (left+right)//2
    baseIdx = 0
    countRoute = 1
    for i in range(1,N):
        if li[i] - li[baseIdx] >= mid:
            countRoute += 1
            baseIdx = i
    if countRoute >= M:
        left = mid + 1
        result = max(mid,result)
    else:
        right = mid - 1
print(result)