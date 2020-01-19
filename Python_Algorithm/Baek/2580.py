import sys
input = sys.stdin.readline

def square(x,y):
    return (x//3)*3 + (y//3)
def isOk(arr,x,y,val):
    ## row&col check
    for i in range(9):
        if arr[i][y] == val or arr[x][i] == val:
            return False

    ## box check
    x_,y_ = x//3 * 3, y//3 * 3
    for i in range(x_,x_+3):
        for j in range(y_,y_+3):
            if arr[i][j] == val:
                return False
    return True

def dfs(arr,i):
    if i == len(zero):
        result = ''
        for j in range(9):
            result += ' '.join(map(str,arr[j]))+'\n'
        print(result)
        exit()
    for p in range(1,10):
        if row[zero[i][0]][p]==0 and col[zero[i][1]][p]==0 and squ[square(zero[i][0],zero[i][1])][p]==0:
            arr[zero[i][0]][zero[i][1]] = p
            row[zero[i][0]][p] = col[zero[i][1]][p] = squ[square(zero[i][0],zero[i][1])][p] = 1
            dfs(arr,i+1)
            arr[zero[i][0]][zero[i][1]] = 0
            row[zero[i][0]][p] = col[zero[i][1]][p] = squ[square(zero[i][0],zero[i][1])][p] = 0
                    

arr = [list(map(int,input().split())) for i in range(9)]
row = [[0 for i in range(10)] for j in range(9)]
col = [[0 for i in range(10)] for j in range(9)]
squ = [[0 for i in range(10)] for j in range(9)]
zero = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            zero.append([i,j])
        else:
            row[i][arr[i][j]] = 1
            col[j][arr[i][j]] = 1
            squ[square(i,j)][arr[i][j]] = 1

dfs(arr,0)

