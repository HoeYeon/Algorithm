N,M = map(int,input().split())
mem = list(map(int,input().split()))
cost = list(map(int,input().split()))
max_cost = sum(cost)+1
dp = [-1 for i in range(max_cost)]
dp[0] = 0

for i in range(N):
    for j in range(max_cost-1,-1,-1):
        if dp[j] != -1:
            dp[j+cost[i]] = max(dp[j+cost[i]],dp[j]+mem[i])
        
for i in range(len(dp)):
    if dp[i] >= M:
        print(i)
        break