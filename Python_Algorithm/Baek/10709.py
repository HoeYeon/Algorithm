import sys
input = sys.stdin.readline
N,M = map(int,input().split())
li = [list(input()[:-1]) for i in range(N)]
ans = ''
for i in li:
    c = -1
    for j in i:
        if j == 'c':
            c = 0
        ans += str(c)+' '
        if c != -1:
            c += 1
    ans += '\n'
print(ans)