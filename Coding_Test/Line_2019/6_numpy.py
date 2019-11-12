import numpy as np


def make_number(n, d):
    ret = np.zeros((2*n - 1, n))

    if d in [0, 2, 3, 5, 7, 8, 9]:
        ret[0, :] = 1
    if d in [0, 4, 5, 6, 8, 9]:
        ret[:n, 0] = 1
    if d in [0, 1, 2, 3, 4, 7, 8, 9]:
        ret[:n, -1] = 1
    if d in [2, 3, 4, 5, 6, 8, 9]:
        ret[n - 1, :] = 1
    if d in [0, 2, 6, 8]:
        ret[n:, 0] = 1
    if d in [0, 1, 3, 4, 5, 6, 7, 8, 9]:
        ret[n:, -1] = 1
    if d in [0, 2, 3, 5, 6, 8]:
        ret[-1, :] = 1

    return ret


def arr2str(arr):
    ret = ''
    for row in arr:
        for c in row:
            ret += '#' if c == 1 else \
                ' ' if c == -1 else '.'
        ret = ret[:-1]
        ret += ' \n'
    return ret


def pad(arr, order, N):
    h, n = arr.shape
    ret = np.zeros((2*N - 1, n + 1))
    if n == N:
        ret[:, :-1] = arr
        ret[:, -1] = -1
        return ret

    pad = N - n

    if order == 'TOP':
        ret[:h, :-1] = arr
    elif order == 'MIDDLE':
        ret[pad:pad+h, :-1] = arr
    elif order == 'BOTTOM':
        ret[-h:, :-1] = arr

    ret[:, -1] = -1
    return ret


n, order = input().split()
n = int(n)
M = -1
numbers = list()

for i in range(n):
    size, num = input().split()
    size = int(size)
    M = max(M, size)
    num = [int(x) for x in num]
    num = [make_number(size, n) for n in num]
    numbers.extend(num)

numbers = [pad(num, order, M) for num in numbers]
last_num = np.concatenate(numbers, axis=1)
print(last_num)
print(arr2str(last_num))
