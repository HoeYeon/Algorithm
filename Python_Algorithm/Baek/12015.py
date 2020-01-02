import bisect
N = int(input())
li = list(map(int,input().split()))
dp = [li[0]]

for i in range(1,N):
    if li[i] > dp[-1]:
        dp.append(li[i])
    else:
        low = bisect.bisect_left(dp,li[i])
        print(low,li[i])
        dp[low] = li[i]
print(dp)
print(len(dp))