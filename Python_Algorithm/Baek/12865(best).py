N, K = map(int, input().split())
dp = [-1 for _ in range(K+1)]
dp[0] = 0
for i in range(N):
    w, v = map(int, input().split())
    for u in range(K-w, -1, -1):
        if dp[u] == -1:
            continue
        dp[u+w] = max(dp[u+w], dp[u]+v)
print(max(dp))
