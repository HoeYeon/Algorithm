N = int(input())
arr = [[0 for i in range(N)] for j in range(N)]
result = 0
def check(x,y):
    #col check
    for i in range(x):
        if arr[i][y] == 1:
            return False
    # left cross check
    x_,y_ = x,y
    while 0 <= x_ <N and 0<=y_<N:
        if arr[x_][y_] == 1:
            return False
        x_ -= 1
        y_ -= 1
    # right cross check
    x_,y_ = x,y
    while 0 <= x_ <N and 0<=y_<N:
        if arr[x_][y_] == 1:
            return False
        x_ -= 1
        y_ += 1
    return True

def dfs(x):
    global result
    if x == N:
        result += 1
        return
    for i in range(N):
        if check(x,i):
            arr[x][i] = 1
            dfs(x+1)
            arr[x][i] = 0
dfs(0)
print(result)
