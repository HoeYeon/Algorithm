n = int(input())

arr = [[' ' for i in range(n+1)] for j in range(n+1)]

def rec(n,x,y):
    if n == 1:
        arr[x][y] = '*'
        return
    div = n//3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            rec(div,x+(div*i), y+(div*j))
    return
rec(n,0,0)
for i in range(n):
    for j in range(n):
        print(arr[i][j],end='')
    print()
