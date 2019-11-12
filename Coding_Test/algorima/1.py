go = [[0,1],[1,0],[-1,0],[0,-1]]
ans = -1
def dfs(board,x,y,check,count):
    global ans
    for i in range(4):
        x_ = x+go[i][0]
        y_ = y+go[i][1]
        if 0<=x_<4 and 0<=y_<4:
            if board[x][y] == board[x_][y_] and check[x_][y_] == 0:
                check[x_][y_] = 1
                dfs(board,x_,y_,check,count+1)
                check[x_][y_] = 0
    ans = max(ans,count)

def solution(board):
    check = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            dfs(board,i,j,check,0)
    answer = -1 if ans == 0 else ans
    return answer
