n, q = map(int, input().split())
ar = [[0]*n for i in range(2)]
k = 0
for rc in range(q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    te = 1 if ar[x][y] == 0 else -1
    ar[x][y] ^= 1
    for i in range(-1, 2):
        if i+y >= 0 and i+y < n and ar[x ^ 1][y+i] == 1:
            k += te
    if not k:
        print("Yes")
    else:
        print("No")
