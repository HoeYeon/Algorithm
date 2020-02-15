import sys
input = sys.stdin.readline
go = [[1,0],[-1,0],[0,1],[0,-1]]
def bfs(queue):
    while len(queue) != 0:
        x,y = queue.pop(0)
        for k in range(4):
            x_,y_ = x+go[k][0], y+go[k][1]
            if 0<=x_<M and 0<=y_<N and li[x_][y_] == 1:
                queue.append([x_,y_])
                li[x_][y_] = -1
    
for i in range(int(input())):
    M,N,K = map(int,input().split())
    li = [[0 for q in range(N)] for p in range(M)]
    for j in range(K):
        x,y = map(int,input().split())
        li[x][y] = 1
    count = 0
    for p in range(M):
        for q in range(N):
            if li[p][q] == 1:
                queue = [[p,q]]
                li[p][q] = -1
                count += 1
                bfs(queue)
    print(count)

