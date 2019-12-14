import sys
import queue

sys.setrecursionlimit(10000)
read = sys.stdin.readline
n = int(input())
mat = [list(map(int,read().split(' '))) for i in range(n)]
q = queue.Queue()
cnt = 0
q.put([[1, 1], [1, 2]])
while q.qsize() > 0:
    tmp = q.get()
    a = tmp[0]
    b = tmp[1]
    if (a[0] == n and a[1] == n) or (b[0] ==n and b[1] == n):
        cnt += 1
        continue
    # row
    if a[0] == b[0] and a[1] != b[1]:
        if a[1]+1 <= n and b[1]+1 <= n and b[0]+1 <= n and mat[b[0]][b[1]] != 1 and mat[b[0]][b[1]-1] != 1 and mat[b[0]-1][b[1]] != 1:
            q.put([[a[0],a[1]+1],[b[0]+1,b[1]+1]])
        if a[1]+1 <= n and b[1]+1 <= n and mat[b[0]-1][b[1]] != 1:
            q.put([[a[0],a[1]+1],[b[0],b[1]+1]])
    # col
    elif a[0] != b[0] and a[1] == b[1]:
        if a[0]+1 <= n and b[1]+1 <= n and b[0]+1 <= n and mat[b[0]][b[1]] != 1 and mat[b[0]][b[1]-1] != 1 and mat[b[0]-1][b[1]] != 1:
            q.put([[a[0]+1,a[1]],[b[0]+1,b[1]+1]])
        if a[0]+1 <= n and b[0]+1 <= n and mat[b[0]][b[1]-1] != 1:
            q.put([[a[0]+1,a[1]],[b[0]+1,b[1]]])
    # else
    else:
        if a[0]+1 <= n and a[1]+1 <= n and b[1]+1 <= n and b[0]+1 <= n and mat[b[0]][b[1]] != 1 and mat[b[0]][b[1]-1] != 1 and mat[b[0]-1][b[1]] != 1:
            q.put([[a[0]+1,a[1]+1],[b[0]+1,b[1]+1]])
        if a[0]+1 <= n and a[1]+1 <= n and b[0]+1 <= n and mat[b[0]][b[1]-1] != 1:
            q.put([[a[0]+1,a[1]+1],[b[0]+1,b[1]]])
        if a[0]+1 <= n and a[1]+1 <= n and b[1]+1 <= n and mat[b[0]-1][b[1]] != 1:
            q.put([[a[0]+1,a[1]+1],[b[0],b[1]+1]])
print(cnt)
