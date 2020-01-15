import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [list(input()[:-1]) for i in range(N)]
p,q = map(int,input().split())
result = [[0 for i in range(M*2)] for j in range(N*2)]

# yflip
for i in range(N):
    for j in range(M):
        result[i][2*M-j-1] = arr[i][j]
        result[i][j] = arr[i][j]
# xflip
for i in range(N,2*N):
    for j in range(2*M):
        result[i][j] = result[2*N-i-1][j]      

result[p-1][q-1] = '#' if result[p-1][q-1] == '.' else '.'
ans = ''
for i in range(N*2):
    ans += ''.join(result[i]) + '\n'
print(ans)