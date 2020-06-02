from math import ceil
N = int(input())
student = list(map(int, input().split()))
B, C = map(int, input().split())
ans = 0
for i in student:
    ans += 1
    ans += ceil((i-B)/C) if i > B else 0

print(ans)
