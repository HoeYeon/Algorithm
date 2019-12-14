N, L = int(input()), list(map(int, input().split()))

if N == 1:
    print(0)
    exit()


def f(a, b):
    st, ed = L[0]+a, L[-1]+b
    if (ed-st) % (N-1) != 0:
        return -1
    d = (ed-st) // (N-1)
    ret = abs(a)+abs(b)
    for i in range(1, N-1):
        if abs(L[i]-st-d*i) > 1:
            return -1
        ret += abs(L[i]-st-d*i)
    return ret

ans = 99999999
for a in range(-1, 2):
    for b in range(-1, 2):
        x = f(a, b)
        if x != -1:
            ans = min(ans, x)
print(ans) if ans != 99999999 else print(-1)
