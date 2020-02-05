# + 300000
check = [0 for i in range(400001)]
N = int(input())
ans = 0
arr = list(map(int,input().split()))
for i in range(N):
    for j in range(i):
        tmp = arr[i] - arr[j]
        if check[tmp+200000]:
            ans += 1
            break
    for j in range(i+1):
        check[arr[i]+arr[j] + 200000] = 1

print(ans)