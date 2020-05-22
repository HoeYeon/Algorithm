N, M = map(int, input().split())
arr = [list(map(int, input())) for i in range(N)]
check = [[0 for i in range(M)] for j in range(N)]
# print(arr)
go = [[1, 0], [0, 1], [-1, 0], [0, -1]]
# isEnd = True
# min_height = 999999999
# height = []


def dfs(arr, x, y, check):
    N = len(arr)
    M = len(arr[0])
    global min_height
    global height
    global isEnd
    height.append(arr[x][y])
    if x == 0 or x == N-1 or y == 0 or y == M-1:
        isEnd = False
    for i in range(4):
        x_ = go[i][0]
        y_ = go[i][1]
        if 0 <= x+x_ < N and 0 <= y+y_ < M and check[x+x_][y+y_] == 0 and min_height > arr[x+x_][y+y_] and arr[x][y] != min_height:
            # print("here", i, x+x_, y+y_, min_height)
            check[x+x_][y+y_] = 1
            min_height = max(min_height, arr[x+x_][y+y_])
            dfs(arr, x+x_, y+y_, check)


ans = 0
for i in range(N):
    for j in range(M):
        min_height = 1
        for k in range(4):
            x = go[k][0]
            y = go[k][1]
            try:
                min_height = max(min_height, arr[i+x][j+y])
            except:
                continue
        # print("i,j,min_height", i, j, min_height)
        if check[i][j] == 0:
            height = []
            isEnd = True
            check[i][j] = 1
            dfs(arr, i, j, check)
            # print("isEnd", isEnd)
            if isEnd:
                # print('height: ', height, min_height)
                for k in height:
                    ans += (min_height-k)
print(ans)
