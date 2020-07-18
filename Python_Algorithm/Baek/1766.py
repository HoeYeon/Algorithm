import heapq

N, M = map(int, input().split())
degree = [0 for i in range(N + 1)]
graph = [[] for i in range(N + 1)]
pq = []
for i in range(M):
    s, e = map(int, input().split())
    degree[e] += 1
    graph[s].append(e)

for i in range(1, N + 1):
    if degree[i] == 0:
        heapq.heappush(pq, i)

ans = ""
while len(pq) != 0:
    node = heapq.heappop(pq)
    ans += str(node) + " "
    for i in graph[node]:
        degree[i] -= 1
        if degree[i] == 0:
            heapq.heappush(pq, i)

print(ans)

