arr = []
def dfs(li,start,end):
    global M
    if M == len(li):
        arr.append(li[:])
        return
    for i in range(start,end+1):
        li.append(str(i))
        dfs(li,i,end)
        li.pop()

N,M = map(int,input().split())
dfs([],1,N)
arr = list(map(' '.join,arr))
print('\n'.join(arr))
