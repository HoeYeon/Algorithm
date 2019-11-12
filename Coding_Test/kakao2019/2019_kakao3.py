from copy import deepcopy

def rotate(m, d):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    if d % 4 == 1:
        for r in range(N):
            for c in range(N):
                ret[c][N-1-r] = m[r][c]
    elif d % 4 == 2:
        for r in range(N):
            for c in range(N):
                ret[N-1-r][N-1-c] = m[r][c]
    elif d % 4 == 3:
        for r in range(N):
            for c in range(N):
                ret[N-1-c][r] = m[r][c]
    else:
        for r in range(N):
            for c in range(N):
                ret[r][c] = m[r][c]
    return ret

def check_ans(m):
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] == 0:
                return False
    return True


def solution(key, lock):
    m = len(key)
    n = len(lock)
    thr = 1-m
    for i in range(4):
        tmp = rotate(key,i)
        for j in range(m+n-1):
            for k in range(m+n-1):
                tmp2 = deepcopy(lock)
                tmp_check = True
                for p in range(m):
                    for q in range(m):
                        if (j+thr+p >=0 and j+thr+p <n) and (k+thr+q >=0 and k+thr+q <n):
                            if tmp2[j+thr+p][k+thr+q] == 0 and tmp[p][q] == 1:
                                tmp2[j+thr+p][k+thr+q] = 1
                            if tmp2[j+thr+p][k+thr+q] == 1 and tmp[p][q] == 1:
                                tmp_check = False
                if check_ans(tmp2) and tmp_check:
                    return True
    return False
