N,K = map(int,input().split())
li = list(map(int,input().split()))
temp = sum(li[:K])
cmp = temp
for i in range(K,N):
    cmp = cmp-li[i-K]+li[i]
    temp = max(temp, cmp)
print(temp)
