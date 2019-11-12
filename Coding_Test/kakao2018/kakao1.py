n = int(input())
prices = [int(input()) for i in range(n)]
d = prices[0:n-1]
for i in range(1,len(d)):
    if d[i] > d[i-1]:
        d[i] = d[i-1]
print(d)
cost = [0 for i in range(n)]
cost[0] = prices[0]
for i in range(1,n):
    dd = d[i-1]
    cost[i] = max(0,prices[i]-dd)
print(sum(cost))
