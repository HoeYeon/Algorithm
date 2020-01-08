import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
li = [list(map(int,input().split())) for i in range(n)]
sj = m
result = m
for i in li:
    sj = sj+ i[0] - i[1]
    if sj < 0:
        result = 0
        break
    result = max(result,sj)
print(result)