import sys
input = sys.stdin.readline

t = int(input())
ans = ''
for i in range(t):
    result = 9999999
    arr = list(map(int,input().split()))
    floor = sorted(list(map(int,input().split())))
    check = [0 for i in range(arr[0]+1)]
    result = min(abs(1-arr[1]),abs(floor[-1]-arr[1]))
    tmp = arr[1]
    for i in floor:
        result = min(result,abs(i-arr[1]))
    ans += str(result) + '\n'
print(ans)