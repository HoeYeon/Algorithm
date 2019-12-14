out = []
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = min((a[i] - a[i - k], a[i]) for i in range(k, n))
    out.append(ans[1] - (ans[0] + 1) // 2)
print(*out)
