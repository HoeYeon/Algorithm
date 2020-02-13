n = int(input())
q = []
go = [[1,0],[-1,0],[0,1],[0,-1]]
li = [list(input()) for i in range(n)]
tot = 0
each = []
for i in range(n):
    for j in range(n):
        if li[i][j] == '1':
            one = 1
            q.append([i,j])
            li[i][j] = '-1'
            while len(q) != 0:
                x,y = q[0][0], q[0][1]
                q.pop(0)
                for k in range(4):
                    x_,y_ = x+go[k][0], y+go[k][1]
                    if 0<=x_<n and 0<=y_<n:
                        if li[x_][y_] == '1':
                            one += 1
                            q.append([x_,y_])
                            li[x_][y_] = '-1'
            each.append(one)
            tot+= 1
print(tot)
print('\n'.join(map(str,sorted(each))))