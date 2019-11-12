'''import itertools

N,M = map(int,input().split())
li = [i for i in range(1,N+1)]
re = list(map(list,itertools.combinations(li,M)))
for i in re:
    print(' '.join(map(str,i)))
'''

N,M = map(int,input().split())
li = [i for i in range(1,N+1)]
check = [0 for i in range(N)]
re = []

def dfs(num,check,tmp):
    global re,li,M

    if num == M:
        aa = tmp[:]
        re.append(aa)
        return

    for i in range(len(li)):
        if check[i] == 0:
            tmp.append(li[i])
            check[i] = 1
            dfs(num+1,check,tmp)
            check[i] = 0
            tmp.pop()

dfs(0,check,[])
for i in re:
    print(' '.join(map(str,i)))
