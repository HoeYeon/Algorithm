go = [[0, 1], [0, -1], [1, 0], [-1, 0]]
answer = 999999999999


def dfs(board, x, y, count, check, b_x, b_y):
    global answer
    if count >= answer:
        return
    N = len(board)
    if x == N-1 and y == N-1:
        answer = min(answer, count)
        return
    for i in go:
        _x = i[0]
        _y = i[1]
        des = [x+_x, y+_y]
        if 0 <= x+_x < N and 0 <= y+_y < N and check[des[0]][des[1]] == 0 and board[des[0]][des[1]] == 0:
            check[des[0]][des[1]] = 1
            if (des[0] == b_x or des[1] == b_y) or b_x == -1:
                if count + 100 < answer:
                    dfs(board, des[0], des[1], count+100, check, x, y,)
            else:
                if count+600 < answer:
                    dfs(board, des[0], des[1], count+600, check, x, y,)
            check[des[0]][des[1]] = 0


def solution(board):
    check = [[0 for i in range(len(board))] for j in range(len(board))]
    check[0][0] = 1
    dfs(board, 0, 0, 0, check, -1, -1)
    return answer
