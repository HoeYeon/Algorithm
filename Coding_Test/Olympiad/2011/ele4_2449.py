N,K = map(int,input().split())
li = list(map(int,input().split()))
arr = [[-1 for j in range(201)] for i in range(201)]
def rec(i,k):
    if i == k:
        return 0
    if arr[i][k] != -1:
        return arr[i][k]
    arr[i][k] = 9999999999
    for j in range(i,k):
        arr[i][k] = min(arr[i][k],rec(i,j) + rec(j+1,k) + (0 if li[i]==li[k] else 1))
    return arr[i][k]

print(rec(0,N-1))
