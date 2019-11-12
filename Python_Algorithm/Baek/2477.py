c = int(input())
li = [[] for i in range(5)]
tmp = []
ttmp = [[1,3],[3,2],[4,1],[2,4]]
size = 0
for i in range(6):
    a,b = map(int,input().split())
    li[a].append(b)
    tmp.append([a,b])

for i in range(len(tmp)):
    for j in ttmp:
if len(li[3]) == 2:
    if len(li[1]) == 2:
        for i in range(len(tmp)):
            if tmp[i][0] == 1 and tmp[(i+1)%len(tmp)][0] == 3:
                size = tmp[i][1] * tmp[(i+1)%len(tmp)][1]
                break
        print((li[4][0] * li[2][0] - size) * c)
    elif len(li[2]) == 2:
        for i in range(len(tmp)):
            if tmp[i][0] == 3 and tmp[(i+1)%len(tmp)][0] == 2:
                size = tmp[i][1] * tmp[(i+1)%len(tmp)][1]
                break
        print((li[4][0] * li[1][0] - size) * c)
elif len(li[4]) == 2:
    if len(li[1]) == 2:
        for i in range(len(tmp)):
            if tmp[i][0] == 4 and tmp[(i+1)%len(tmp)][0] == 1:
                size = tmp[i][1] * tmp[(i+1)%len(tmp)][1]
                break
        print((li[3][0] * li[2][0] - size) * c)
    elif len(li[2]) == 2:
        for i in range(len(tmp)):
            if tmp[i][0] == 2 and tmp[(i+1)%len(tmp)][0] == 4:
                size = tmp[i][1] * tmp[(i+1)%len(tmp)][1]
                break
        print((li[3][0] * li[1][0] - size) * c)
