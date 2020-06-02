N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
cmd = list(map(int, input().split()))
cur = 6
go = [[0, 1], [0, -1], [-1, 0], [1, 0]]
dice = {
    1: {'v': 0, 'p': 6, 3: 2, 4: 5, 1: 3, 2: 4},
    2: {'v': 0, 'p': 5, 3: 6, 4: 1, 1: 3, 2: 4},
    3: {'v': 0, 'p': 4, 3: 2, 4: 5, 1: 4, 2: 1},
    4: {'v': 0, 'p': 3, 3: 2, 4: 5, 1: 1, 2: 3},
    5: {'v': 0, 'p': 2, 3: 1, 4: 6, 1: 3, 2: 4},
    6: {'v': 0, 'p': 1, 3: 5, 4: 2, 1: 3, 2: 4}
}

for i in cmd:
    _x, _y = go[i-1][0], go[i-1][1]
    if 0 <= x+_x < N and 0 <= y+_y < M:
        x += _x
        y += _y
        cur = dice[cur][i]
        if arr[x][y] == 0:
            arr[x][y] = dice[cur]['v']
            print('cur:', cur, 'dice: ', dice[cur], dice[dice[cur]['p']]['v'])
        else:
            dice[cur]['v'] = arr[x][y]
            arr[x][y] = 0
            print('cur:', cur, 'dice: ', dice[cur], dice[dice[cur]['p']]['v'])
