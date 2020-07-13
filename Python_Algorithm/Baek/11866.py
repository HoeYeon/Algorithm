from collections import deque

N, K = map(int, input().split())
q = deque([i + 1 for i in range(N)])
ans = "<"
count = 0
while True:
    if len(q) == 1:
        ans += str(q.popleft()) + ">"
        break
    if count == K - 1:
        ans += str(q.popleft()) + ", "
        count = 0
        continue
    count += 1
    q.append(q.popleft())
print(ans)
