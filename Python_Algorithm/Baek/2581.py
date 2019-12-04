M = int(input())
N = int(input())
MAX = 10001
arr = [i for i in range(MAX)]
arr[1] = 0
for i in range(2,MAX):
    if arr[i] == 0:
        continue
    for j in range(i*2,MAX,i):
        arr[j] = 0

prime = [i for i in range(M,N+1) if arr[i] == i]
if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))
