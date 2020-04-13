import sys
input = sys.stdin.readline
T = int(input())
result = 0
check = False


def row_col_check(x, y, arr, target):
    col = [row[y] for row in arr]
    if target in arr[x]:
        return False
    elif target in col:
        return False
    else:
        return True


def dfs(arr, x, y, N, K):
    global check
    if check:
        return
    if x == N-1 and y == N-1:
        trace = 0
        for i in range(N):
            trace += arr[i][i]
        if trace == K:
            check = True
            print("POSSIBLE")
            result = [[str(y) for y in x] for x in arr]
            result = '\n'.join([' '.join(x) for x in result])
            print(result)
        return
    for i in range(1, N+1):
        tmp = 0
        for j in range(x):
            tmp += arr[j][j]
        if K-tmp > N*(N-x-1):
            continue
        if check:
            break
        if y == N-1:
            if row_col_check(x+1, 0, arr, i):
                arr[x+1][0] = i
                dfs(arr, x+1, 0, N, K)
                arr[x+1][0] = 0
        else:
            if row_col_check(x, y+1, arr, i):
                arr[x][y+1] = i
                dfs(arr, x, y+1, N, K)
                arr[x][y+1] = 0


for _ in range(T):
    print("Case #{}: ".format(_+1), end='')
    check = False
    result = []
    N, K = map(int, input().split())
    arr = [[0 for j in range(N)] for i in range(N)]
    arr[0][0] = 1
    dfs(arr, 0, 0, N, K)

    if not check:
        print("IMPOSSIBLE")
