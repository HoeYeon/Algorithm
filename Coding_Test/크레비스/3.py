# U D L R
go = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}
check = [[0, 0], [0, 1], [1, 1], [1, 0]]


def solution(moves):
    N = len(moves)*2 + 1
    mat = [[[] for i in range(N)] for j in range(N)]
    answer = 0
    x, y = len(moves), len(moves)
    for i in moves:
        _x, _y = go[i]
        if [x, y] not in mat[x+_x][y+_y]:
            mat[x+_x][y+_y].append([x, y])
        if [x+_x, y+_y] not in mat[x][y]:
            mat[x][y].append([x+_x, y+_y])
        x = x+_x
        y = y+_y
    for i in range(N-1):
        for j in range(N-1):
            isSquare = True
            for k, v in enumerate(check):
                bx, by = v
                ax, ay = check[k-1]
                if [i+ax, j+ay] not in mat[i+bx][j+by]:
                    isSquare = False
                    break
            if isSquare:
                answer += 1
    return answer
