import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    arr = [[] for i in range(N)]
    result = [0 for i in range(N)]
    C = J = 0
    check = True
    for i in range(N):
        tmp = list(map(int, input().split()))
        tmp.append(i)
        arr[i].extend(tmp)
    arr.sort()
    for i in arr:
        if C <= i[0]:
            C = i[1]
            result[i[2]] = 'C'
        elif J <= i[0]:
            J = i[1]
            result[i[2]] = 'J'
        else:
            check = False
            break
    print("Case #{}: {}".format(_+1, ''.join(result) if check else "IMPOSSIBLE"))
