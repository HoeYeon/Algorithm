N,M = map(int,input().split())
cost = [int(input()) for i in range(N)]
ans = [0 for i in range(N)]
judge = [int(input()) for i in range(M)]
for i in judge:
    for j in range(N):
        if cost[j] <= i:
            ans[j] += 1
            break
print(ans.index(max(ans))+1)
