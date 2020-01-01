import sys

input = sys.stdin.readline

result = ''
for i in range(int(input())):
    h,m = map(int,input().split())
    ans = (24-h)*60 - m
    result += str(ans) + '\n'
print(result)