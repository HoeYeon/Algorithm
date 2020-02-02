N,K = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(N)]
dp = [[0,0] for i in range(K+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(K,-1,-1):
        w = j + arr[i][0]
        if dp[j][0] == 1 and w <= K:
            dp[w][1] = max(dp[w][1], dp[j][1] + arr[i][1])
            dp[w][0] = 1
print(max(dp)[1])
