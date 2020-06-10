import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
shark = {'size': 2, 'eat': 0, 'loc': [-1, -1]}
arr = []
go = [[-1, 0], [0, -1], [0, 1], [1, 0]]
dis = 0
for i in range(N):
    line = list(map(int, input().split()))
    arr.append(line)
    if 9 in line:
        shark['loc'] = [i, line.index(9)]

while True:
    path = deque()
    check = [[0 for i in range(N)] for j in range(N)]
    path.append([shark['loc'][0], shark['loc'][1], 1])
    check[shark['loc'][0]][shark['loc'][1]] = 1
    findTarget = False
    target = []
    targetCount = 0
    while len(path) != 0:
        x, y, count = path.popleft()
        if findTarget and count != targetCount:
            break
        for i in range(4):
            _x, _y = go[i][0], go[i][1]
            if findTarget:
                if 0 <= x+_x < N and 0 <= y+_y < N and check[x+_x][y+_y] == 0:
                    if arr[x+_x][y+_y] < shark['size'] and arr[x+_x][y+_y] != 0:
                        check[x+_x][y+_y] = 1
                        target.append([x+_x, y+_y])
            elif 0 <= x+_x < N and 0 <= y+_y < N and check[x+_x][y+_y] == 0:
                if arr[x+_x][y+_y] == 0:
                    check[x+_x][y+_y] = 1
                    path.append([x+_x, y+_y, count+1])
                elif arr[x+_x][y+_y] < shark['size']:
                    findTarget = True
                    target.append([x+_x, y+_y])
                    targetCount = count
                    check[x+_x][y+_y] = 1
                elif arr[x+_x][y+_y] == shark['size']:
                    check[x+_x][y+_y] = 1
                    path.append([x+_x, y+_y, count+1])
                elif arr[x+_x][y+_y] > shark['size']:
                    continue
    if findTarget:
        target = sorted(target, key=lambda x: x[0])
        if len(target) > 1 and target[0][0] == target[1][0]:
            tmp = target[0][0]
            target = filter(lambda x: x[0] == tmp, target)
            target = sorted(target, key=lambda x: x[1])
        tX, tY = target[0]
        sX, sY = shark['loc']
        dis += targetCount
        arr[tX][tY] = 0
        arr[sX][sY] = 0
        if shark['size'] == shark['eat']+1:
            shark['size'] += 1
            shark['eat'] = 0
        else:
            shark['eat'] += 1
        shark['loc'] = [tX, tY]
    else:
        break

print(dis)
