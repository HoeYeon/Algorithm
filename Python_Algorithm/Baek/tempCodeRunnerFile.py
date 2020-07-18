import heapq

N, M = map(int, input().split())
arr = [[i + 1, i + 1, i + 1] for i in range(N)]
ques = sorted([list(map(int, input().split())) for i in range(M)], key=lambda x: x[0])
for _ in ques:
    s, e = _
    arr[s - 1][0] = arr[e - 1][0]
    arr[s - 1][1] = arr[e - 1][1] - 1
arr = sorted(arr, key=lambda x: (x[0], x[1]))
ans = ""
for i in arr:
    ans += str(i[2]) + " "
print(ans)
