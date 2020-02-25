from heapq import heappop, heappush
import sys


def dijkstra(arr, start):
    dist = arr[:]
    dist[start] = 0
    heappush(node, [0, start])
    while len(node) != 0:
        item = heappop(node)
        for value in info[item[1]]:
            if dist[value[1]] > value[0] + dist[item[1]]:
                dist[value[1]] = value[0] + dist[item[1]]
                heappush(node, [dist[value[1]], value[1]])
    return dist


input = sys.stdin.readline
V, E = map(int, input().split())
MAX = 99999999
node = []
info = [[] for i in range(V+1)]
dist = [MAX] * (V+1)
for i in range(E):
    u, v, w = map(int, input().split())
    info[u].append([w, v])
    info[v].append([w, u])
p, q = map(int, input().split())
c1 = dijkstra(dist, 1)
c2 = dijkstra(dist, p)
c3 = dijkstra(dist, q)
ans = min((c1[p]+c2[q]+c3[V]), (c1[q]+c3[p]+c2[V]))
print(-1 if ans >= MAX or
      ans < 0 else ans)
