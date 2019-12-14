N = int(input())
li = list(map(int, input().split()))
dp = [1 for i in range(N)]

for i in range(N):
    for j in range(i, -1, -1):
        if li[i] > li[j] and dp[i] <= dp[j]:
            dp[i] = dp[j]+1
print(max(dp))

'''n = int(input())
x = list(map(int, input().split()))
ans = []
for y in x:
    idx = 0
    while idx < len(ans):
        if y <= ans[idx]:
            ans[idx] = y
            break
        else:
            idx += 1
    if idx == len(ans):
        ans.append(y)

print(len(ans))
print(ans)'''
