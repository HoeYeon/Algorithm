import sys
input = sys.stdin.readline
N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
cmd = list(map(int, input().split()))
cur = 6
go = [[0, 1], [0, -1], [-1, 0], [1, 0]]
# 1:동, 2:서, 3:북, 4:남
# 초기위치 1,2,3,4,5,6
dice = [-1, 0, 0, 0, 0, 0, 0]
ans = ''
for i in cmd:
    _x, _y = go[i-1][0], go[i-1][1]
    if 0 <= x+_x < N and 0 <= y+_y < M:
        x += _x
        y += _y
        if i == 1:
            dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
        elif i == 2:
            dice[1], dice[3], dice[6], dice[4] = dice[4], dice[1], dice[3], dice[6]
        elif i == 3:
            dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
        elif i == 4:
            dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
        if arr[x][y] == 0:
            arr[x][y] = dice[1]
            print(dice[6])
        else:
            dice[1] = arr[x][y]
            arr[x][y] = 0
            print(dice[6])
