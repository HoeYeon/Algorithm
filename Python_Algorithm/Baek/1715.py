import sys
import heapq

input = sys.stdin.readline
N = int(input())
cost = 0
arr = sorted([int(input()) for i in range(N)])
while len(arr)>1:
    tmp = heapq.heappop(arr) + heapq.heappop(arr)
    cost += tmp
    heapq.heappush(arr,tmp)
print(cost)

