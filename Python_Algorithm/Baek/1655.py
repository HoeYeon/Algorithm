import sys
from math import log
input = sys.stdin.readline
import heapq

heap = []

N = int(input())
result = ''
for i in range(1,N+1):
    tmp = int(input())
    heapq.heappush(heap,tmp)
    tt = heap[:]
    thr = i//2-1 if i%2 ==0 else i//2
    if i%2 ==0:
        ans = min(tt[thr],tt[thr+1])
    else:
        ans = tt[thr]
    result += str(ans) + '\n'
print(result)