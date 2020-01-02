'''N = int(input())
li = list(map(int, input().split()))
dp = [1 for i in range(N)]

for i in range(N):
    for j in range(i, -1, -1):
        if li[i] > li[j] and dp[i] <= dp[j]:
            dp[i] = dp[j]+1
print(max(dp))
'''
## More fast Version ##
N = int(input())
li = list(map(int,input().split()))
dp = [li[0]]

for i in range(1,N):
    if li[i] > dp[-1]:
        dp.append(li[i])
    else:
        j = len(dp)-1
        while j > 0:
            if dp[j-1] < li[i]:
                break
            j -= 1
        dp[j] = li[i]
print(len(dp))
