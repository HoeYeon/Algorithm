idx,ans = -1,-1
def dfs(arr,check,num,s):
    for i in arr[num]:
        if check[i] == 0:
            check[i] = 1
            dfs(arr,check,i,s+li[i])
            check[i] = 0
    global idx
    global ans
    if ans <= s:
        idx, ans = num, s

N = int(input())
li = list(map(int,input().split()))
arr = [[] for i in range(N)]
check = [0 for i in range(N)]

for i in range(N-1):
    a,b = map(int,input().split())
    arr[a-1].append(b-1)
    arr[b-1].append(a-1)
check[0] = 1
dfs(arr,check,0,li[0])
print(idx+1,ans)
