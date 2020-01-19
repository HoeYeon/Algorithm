import sys
input = sys.stdin.readline

n,q = map(int,input().split())
arr = [[0 for i in range(n)] for j in range(2)]
check = []
result = ''
for i in range(q):
    x,y = map(int,input().split())
    x,y = x-1,y-1
    arr[x][y] = 0 if arr[x][y] == 1 else 1
    if x == 0:
        check.append(y)
    check = list(set(check))
    c = False
    for i in check:
        y = i
        x = 1
        if arr[0][i] == 1 and ((y > 0 and arr[x][y-1] == 1) or arr[x][y] == 1 or (y<n-1 and arr[x][y+1] ==1)):
            c = True
    if c:
        result += 'No\n'
    else:
        result += 'Yes\n'
print(result)