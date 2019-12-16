from functools import reduce
for i in range(int(input())):
    n = int(input())
    if n == 0:
        print(0)
        continue
    d = {}
    for j in range(n):
        kind = list(input().split())[1]
        d[kind] = d[kind] + 1 if kind in d else 2
    print(reduce(lambda x, y: x*y, d.values())-1)
