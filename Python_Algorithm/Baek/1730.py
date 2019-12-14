n = int(input())
a = [[0] * n for _ in range(n)]
x = y = 0
for t in input():
	if t == 'L' and y:
		a[x][y] |= 1
		y -= 1
		a[x][y] |= 1
	if t == 'R' and y + 1 < n:
		a[x][y] |= 1
		y += 1
		a[x][y] |= 1
	if t == 'U' and x:
		a[x][y] |= 2
		x -= 1
		a[x][y] |= 2
	if t == 'D' and x + 1 < n:
		a[x][y] |= 2
		x += 1
		a[x][y] |= 2
for i in range(n):
    for j in range(n):
        if a[i][j] == 0:
            a[i][j] = '.'
        elif a[i][j] == 1:
            a[i][j] = '-'
        elif a[i][j] == 2:
            a[i][j] = '|'
        elif a[i][j] == 3:
            a[i][j] = '+'
for i in a:
    print(''.join(i))
