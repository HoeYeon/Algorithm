from sys import stdin
N,M = map(int,input().split())

li = [int(x) for x in stdin.read().splitlines()]

left = 1
right = max(li)

while left <= right:
    mid = (left+right)//2
    cnt = 0
    for i in li:
        cnt += i//mid
    if cnt >= M:
        left = mid+1
        result = mid
    else:
        right = mid-1
print(result)