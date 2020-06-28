from collections import deque
import sys

input = sys.stdin.readline


def bfs(arr):
    count = 0
    check = [[0 for i in range(N)] for j in range(N)]
    q = deque()
    for i in range(N):
        for j in range(N):
            if check[i][j] == 0:
                q.append([i, j])
                check[i][j] = 1
                while len(q) != 0:
                    x, y = q.popleft()
                    for k in range(4):
                        _x, _y = go[k][0], go[k][1]
                        t_x = x + _x
                        t_y = y + _y
                        if 0 <= t_x < N and 0 <= t_y < N and check[t_x][t_y] == 0:
                            if arr[t_x][t_y] == arr[x][y]:
                                check[t_x][t_y] = 1
                                q.append([t_x, t_y])
                count += 1
    return count


N = int(input())
go = [[0, 1], [1, 0], [-1, 0], [0, -1]]
arr = [list(input()) for i in range(N)]
arr2 = [[] for i in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == "G":
            arr2[i].append("R")
        else:
            arr2[i].append(arr[i][j])

isRGB = bfs(arr)
isRB = bfs(arr2)
print(isRGB, isRB)
