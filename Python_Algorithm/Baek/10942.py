import sys

input = sys.stdin.readline
N = int(input())
arr = [-1] + list(map(int, input().split()))
M = int(input())
dp = [[1 for j in range(N + 1)] for i in range(N + 1)]
for i in range(N):
    dp[2][i] = 1 if arr[i] == arr[i + 1] else 0

for i in range(3, N + 1):
    for j in range(1, N - i + 2):
        dp[i][j] = 1 if dp[i - 2][j + 1] == 1 and arr[j] == arr[j + i - 1] else 0

ans = ""
for question in range(M):
    S, E = map(int, input().split())
    ans += str(dp[E - S + 1][S]) + "\n"
print(ans)
