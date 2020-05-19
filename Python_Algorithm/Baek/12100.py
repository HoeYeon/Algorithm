from copy import deepcopy


def dfs(arr2, count):
    global max_num
    N = len(arr2)
    mm = max(map(max, arr2))
    if mm > max_num:
        max_num = mm
    if count == 5:
        return
    for i in range(4):
        arr = deepcopy(arr2)
        # up
        if i == 0:
            for j in range(N):
                tmp = [0 for k in range(N)]
                k = 0
                tt = 1
                t_idx = 0
                while k < N-1 and tt < N:
                    if arr[k][j] == 0:
                        k += 1
                        tt += 1
                        continue
                    if arr[tt][j] == 0:
                        while tt < N-1 and arr[tt][j] == 0:
                            tt += 1
                    if arr[k][j] == arr[tt][j]:
                        tmp[t_idx] = 2*arr[k][j]
                        k = tt+1
                        tt += 2
                        t_idx += 1
                    else:
                        tmp[t_idx] = arr[k][j]
                        k = tt
                        tt += 1
                        t_idx += 1
                if k == N-1 and arr[k][j] != 0:
                    tmp[t_idx] = arr[k][j]
                for k in range(N):
                    arr[k][j] = tmp[k]
            dfs(arr, count+1)
        # down
        elif i == 1:
            for j in range(N):
                tmp = [0 for k in range(N)]
                k = N - 1
                tt = N - 2
                t_idx = N-1
                while k > 0 and tt >= 0:
                    if arr[k][j] == 0:
                        k -= 1
                        tt -= 1
                        continue
                    if arr[tt][j] == 0:
                        while tt > 0 and arr[tt][j] == 0:
                            tt -= 1
                    if arr[k][j] == arr[tt][j]:
                        tmp[t_idx] = 2*arr[k][j]
                        k = tt-1
                        tt -= 2
                        t_idx -= 1
                    else:
                        tmp[t_idx] = arr[k][j]
                        k = tt
                        tt -= 1
                        t_idx -= 1
                if k == 0 and arr[k][j] != 0:
                    tmp[t_idx] = arr[k][j]
                for k in range(N):
                    arr[k][j] = tmp[k]
            dfs(arr, count+1)
        # right
        elif i == 2:
            for j in range(N):
                tmp = [0 for k in range(N)]
                k = N - 1
                tt = N - 2
                t_idx = N-1
                while k > 0 and tt >= 0:
                    if arr[j][k] == 0:
                        k -= 1
                        tt -= 1
                        continue
                    if arr[j][tt] == 0:
                        while tt > 0 and arr[j][tt] == 0:
                            tt -= 1
                    if arr[j][k] == arr[j][tt]:
                        tmp[t_idx] = 2*arr[j][k]
                        k = tt-1
                        tt -= 2
                        t_idx -= 1
                    else:
                        tmp[t_idx] = arr[j][k]
                        k = tt
                        tt -= 1
                        t_idx -= 1
                if k == 0 and arr[j][k] != 0:
                    tmp[t_idx] = arr[j][k]
                for k in range(N):
                    arr[j][k] = tmp[k]
            dfs(arr, count+1)
        # left
        else:
            for j in range(N):
                tmp = [0 for k in range(N)]
                k = 0
                tt = 1
                t_idx = 0
                while k < N-1 and tt < N:
                    if arr[j][k] == 0:
                        k += 1
                        tt += 1
                        continue
                    if arr[j][tt] == 0:
                        while tt < N-1 and arr[j][tt] == 0:
                            tt += 1
                    if arr[j][k] == arr[j][tt]:
                        tmp[t_idx] = 2*arr[j][k]
                        k = tt+1
                        tt += 2
                        t_idx += 1
                    else:
                        tmp[t_idx] = arr[j][k]
                        k = tt
                        tt += 1
                        t_idx += 1
                if k == N-1 and arr[j][k] != 0:
                    tmp[t_idx] = arr[j][k]
                for k in range(N):
                    arr[j][k] = tmp[k]
            dfs(arr, count+1)


N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
max_num = -1
dfs(arr, 0)

print(max_num)
