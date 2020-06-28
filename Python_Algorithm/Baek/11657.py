MAX = 9999999999
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(M)]
dist = [MAX for i in range(N + 1)]
dist[1] = 0
check = True
ans = ""
for i in range(1, N + 1):
    for edge in edges:
        here, to, weight = edge
        if dist[here] == MAX:
            continue
        dist[to] = min(dist[to], dist[here] + weight)

# 음수 사이클 체크
for edge in edges:
    here, to, weight = edge
    if dist[here] == MAX:
        continue
    if dist[to] > dist[here] + weight:
        check = False
        break
if not check:
    print(-1)
else:
    for i in range(2, len(dist)):
        ans += str(-1) + "\n" if dist[i] == MAX else str(dist[i]) + "\n"
    print(ans)

