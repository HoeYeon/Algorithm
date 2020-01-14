import sys
input = sys.stdin.readline

N = int(input())
a,b = map(int,input().split())
dp = [[0 for j in range(N)] for i in range(N)]
arr = [a,b]
for i in range(N-1):
    a,b = map(int,input().split())
    arr.append(b)

for l in range(1,N):
    for i in range(N-l):
        j = i+l
        dp[i][j] = 999999999999
        for k in range(i,j):
            q = dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j]
            if q < dp[i][j]:
                dp[i][j] = q
print(dp[0][N-1])