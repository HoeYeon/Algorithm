go = [[0, 1], [1, 0], [0, -1], [-1, 0]]
ans = 0


def dfs(N, M, arr, check, x, y):
    global ans
    for i in range(4):
        xx = go[i][0]
        yy = go[i][1]
        if 0 <= x + xx < N and 0 <= y + yy < M:
            if arr[x + xx][y + yy] == "0":
                ans += 1
            elif arr[x + xx][y + yy] == "1" and check[x + xx][y + yy] == 0:
                check[x + xx][y + yy] = 1
                dfs(N, M, arr, check, x + xx, y + yy)


arr = [i.split() for i in input().split(";")]
N = len(arr)
M = len(arr[0])
check = [[0 for i in range(M)] for j in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == "1" and check[i][j] == 0:
            check[i][j] = 1
            dfs(N, M, arr, check, i, j)
print(ans)

