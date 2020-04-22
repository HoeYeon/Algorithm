# x+1, x-1, 2*x

from collections import deque
n, k = map(int, input().split())
queue = deque([[n, 0]])
check = [0 for i in range(100001)]
check[n] = 1

while True:
    tmp = queue.popleft()
    loc, count = tmp[0], tmp[1]
    if loc == k:
        print(count)
        break
    if loc-1 >= 0 and check[loc-1] == 0:
        queue.append([loc-1, count+1])
        check[loc-1] = 1
    if loc+1 <= 100000 and loc+1 <= k and check[loc+1] == 0:
        queue.append([loc+1, count+1])
        check[loc+1] = 1
    if loc*2 <= 100000 and loc*2 <= k and check[loc*2] == 0:
        queue.append([loc*2, count+1])
        check[loc*2] = 1
