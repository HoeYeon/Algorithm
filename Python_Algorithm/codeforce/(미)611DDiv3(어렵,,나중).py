import sys
from math import ceil
from collections import Counter
input = sys.stdin.readline

N,M = map(int,input().split())
tree = sorted(list(map(int,input().split())))
d = Counter(tree)
empty = tree[-1] - tree[0] + 1 - N
tot = M-empty
left = tot//2
right = ceil(tot/2)
print(tot,left,right)
result = [i for i in range(tree[0]-left,tree[-1]+right+1)]
## getSum
ans = 0
first = tree[0]
sec = tree[1]
idx = 1
for i in range(tree[0]+1,tree[-1]):
    if d[i] != 0:
        idx += 1
        first = sec
        sec = tree[idx]
        continue
    '''if i > sec:
        idx += 1
        first = sec
        sec = tree[idx]'''
    ans += min(i-first,sec-i)
ans += (sum([i for i in range(left+1)]) + sum([i for i in range(right+1)]))
print(ans)
result = list(set(result) - set(tree))
result = sorted(list(map(str,result)))
print(' '.join(result))