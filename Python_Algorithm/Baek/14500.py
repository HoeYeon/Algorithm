import sys
input = sys.stdin.readline
ans = -1
go = [[1, 0], [-1, 0], [0, 1], [0, -1]]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
check = [[0 for i in range(M)] for j in range(N)]


def dfs(arr, size, count, x, y, check):
    global ans
    if size == 4:
        ans = max(ans, count)
        return

    # check mountain structure
    tmp = arr[x][y]
    for i in range(4):
        x1, x2, x3 = x+go[i][0], x+go[(i+1) % 4][0], x+go[(i+2) % 4][0]
        y1, y2, y3 = y+go[i][1], y+go[(i+1) % 4][1], y+go[(i+2) % 4][1]
        if 0 <= x1 < N and 0 <= x2 < N and 0 <= x3 < N and 0 <= y1 < M and 0 <= y2 < M and 0 <= y3 < M:
            ans = max(ans, tmp + arr[x1][y1]+arr[x2][y2]+arr[x3][y3])

    for i in range(4):
        if size == 0 and (i == 1):
            continue
        _x = go[i][0]
        _y = go[i][1]
        if 0 <= x+_x < N and 0 <= y+_y < M and check[x+_x][y+_y] == 0:
            check[x+_x][y+_y] = 1
            dfs(arr, size+1, count+arr[x+_x][y+_y], x+_x, y+_y, check)
            check[x+_x][y+_y] = 0


for i in range(N):
    for j in range(M):
        check[i][j] = 1
        dfs(arr, 0, 0, i, j, check)
        check[i][j] = 0

print(ans)
