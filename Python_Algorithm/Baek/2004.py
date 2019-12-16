n,m = map(int,input().split())
arr = [0 for i in range(n+1)]
for i in range(n-m,n+1):
    arr[i] = arr[i-1]
    idx = i
    if i%5 == 0:
        while i % 5 == 0:
            i //=5
            arr[idx] += 1
print(arr[n])
