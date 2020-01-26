N,M = map(int,input().split())
tmp = [input() for i in range(N)]
arr = [list('.'*(M+2)) for i in range(N+2)]

go = [[1,0],[-1,0],[0,1],[0,-1]]
def check(x,y):
    count = 0
    for i in range(4):
        x_,y_ = x+go[i][0], y+go[i][1]
        if arr[x_][y_] == '.':
            count += 1
    return True if count >=3 else False

for i in range(1,N+1):
    for j in range(1,M+1):
        arr[i][j] = tmp[i-1][j-1]

for i in range(1,N+1):
    for j in range(1,M+1):
        if check(i,j):
            arr[i][j] = '@' if arr[i][j] == 'X' else '.'
## rowcheck
minrow,maxrow = 99999,-1
mincol,maxcol = 99999,-1
for i in range(N+2):
    for j in range(M+2):
        if arr[i][j] == 'X':
            minrow = min(minrow,i)
            maxrow = max(maxrow,i)
            mincol = min(mincol,j)
            maxcol = max(maxcol,j)
result = ''
for i in range(minrow,maxrow+1):
    for j in range(mincol,maxcol+1):
        result += arr[i][j] if arr[i][j] == 'X' else '.'
    result += '\n'
print(result)