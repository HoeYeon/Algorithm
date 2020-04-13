import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    trace = k = c = 0
    # get Trace
    for i in range(N):
        trace += arr[i][i]
    # get row
    for i in range(N):
        if len(list(set(arr[i]))) != len(arr[i]):
            k += 1
    # get col
    for i in range(N):
        col = [row[i] for row in arr]
        if len(list(set(col))) != len(col):
            c += 1
    print('Case #{}: {} {} {}'.format(_+1, trace, k, c))
