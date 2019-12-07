N = int(input())
num = list(map(int,input().split()))
oper = list(map(int,input().split()))
maxx = -1000000001
minn = 1000000001
def dfs(oper,s,end):
    global maxx
    global minn

    if sum(oper) == 0:
        maxx = max(maxx,s)
        minn = min(minn,s)
        return
    for i in range(len(oper)):
        if oper[i] == 0:
            continue
        tmp = s
        #더하기
        if i == 0:
            s += num[end]
        elif i==1:
            s -= num[end]
        elif i ==2:
            s *= num[end]
        else:
            s = abs(s)//abs(num[end])*-1 if s < 0 or num[end] < 0 else s//num[end]
        oper[i] -= 1
        dfs(oper,s,end+1)
        oper[i] += 1
        s = tmp
dfs(oper,num[0],1)
print(maxx,minn)
