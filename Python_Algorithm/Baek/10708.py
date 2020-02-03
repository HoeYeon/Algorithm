from collections import Counter
N = int(input())
M = int(input())
arr = list(map(int,input().split()))
ans = [0 for i in range(N)]
for i in range(M):
    li = list(map(int,input().split()))
    for j in range(len(li)):
        if arr[i] == li[j]:
            ans[j] += 1
    ans[arr[i]-1] += N-li.count(arr[i])
print('\n'.join(map(str,ans)))