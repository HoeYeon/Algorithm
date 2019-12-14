N = int(input())
go = [[0, 1], [1, 0], [0, -1], [-1, 0]]
mat = [[0 for j in range(N)] for i in range(N)]
snake = [[0, 0]]
cmnd = [0 for i in range(10001)]
for i in range(int(input())):
    x, y = map(int, input().split())
    mat[x-1][y-1] = 1
for i in range(int(input())):
    t, c = input().split()
    cmnd[int(t)] = c

time = 1
way = 0
while True:
    head = snake[-1][:]
    x, y = head[0] + go[way][0], head[1] + go[way][1]
    if [x, y] in snake or x>=N or y>=N or x<0 or y<0:
        break
    if mat[x][y] == 0:
        snake = snake[1:]
    else:
        mat[x][y] = 0
    snake.append([x,y])
    if cmnd[time] == 'D':
        way = (way+1)%4
    elif cmnd[time] == 'L':
        way = (way-1)%4
    time += 1
print(time)
