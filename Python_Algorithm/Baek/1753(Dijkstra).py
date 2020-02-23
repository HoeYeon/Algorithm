from heapq import heappop, heappush
import sys
input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
MAX = 99999999
node = []
info = [[] for i in range(V+1)]
dist = [MAX] * (V+1)
for i in range(E):
    u, v, w = map(int, input().split())
    info[u].append([w, v])
dist[K] = 0
heappush(node, [0, K])
while len(node) != 0:
    item = heappop(node)
    for i, value in enumerate(info[item[1]]):
        if dist[value[1]] > value[0] + dist[item[1]]:
            dist[value[1]] = value[0] + dist[item[1]]
            heappush(node, [dist[value[1]], value[1]])
result = ''
for i in range(1, len(dist)):
    result += str(dist[i]) if dist[i] != MAX else "INF"
    result += '\n'
print(result)
