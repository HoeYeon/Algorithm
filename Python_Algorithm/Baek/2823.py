N,M = map(int,input().split())
arr = [list(input()) for i in range(N)]
go = [[1,0],[-1,0],[0,1],[0,-1]]
check = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == '.':
            cnt = 0
            for k in go:
                x = i + k[0]
                y = j + k[1]
                if N > x >= 0 and M > y >= 0:
                    if arr[x][y] == '.':
                        cnt += 1
            if cnt < 2:
                check = 1
print(1 if check else 0)