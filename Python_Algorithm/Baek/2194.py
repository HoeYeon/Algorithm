from collections import deque
import sys
input = sys.stdin.readline

go = [[1, 0], [0, 1], [-1, 0], [0, -1]]
N, M, A, B, K = map(int, input().split())
mat = [[0 for i in range(M)] for j in range(N)]
# check = [[0 for i in range(M)] for j in range(N)]
for i in range(K):
    a, b = map(int, input().split())
    mat[a-1][b-1] = 1
start = list(map(lambda x: x-1, map(int, input().split())))
end = list(map(lambda x: x-1, map(int, input().split())))

# for i in range(A):
#     for j in range(B):
#         mat[i+start[0]-1][j+start[1]-1] = 2
#         check[i+start[0]-1][j+start[1]-1] = 1
#         mat[i+end[0]-1][j+end[1]-1] = 3
print(mat)
mat[start[0]][start[1]] = 2
queue = deque([[start, 0]])
try:
    while True:
        # print("hello")
        tmp = queue.popleft()
        loc, count = tmp[0], tmp[1]
        # print(loc)
        if loc == end:
            print(count)
            break
        for i in range(4):
            x, y = go[i][0], go[i][1]
            ch = False
            for p in range(A):
                if ch:
                    break
                for q in range(B):
                    if (0 <= loc[0]+x+p < N and 0 <= loc[1]+y+q < M and
                            mat[loc[0]+x+p][loc[1]+y+q] != 1 and mat[loc[0]+x][loc[1]+y] == 0):
                        continue
                    else:
                        ch = True
            if ch == False:
                queue.append([[loc[0]+x, loc[1]+y], count+1])
                mat[loc[0]+x][loc[1]+y] = 2
except:
    print(-1)
