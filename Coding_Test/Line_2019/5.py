arr = [ [0 for j in range(51)]for i in range(51)]

for i in range(49):
    for j in range(i+1):
        if i==0 or j == 0:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

x,y = map(int,input().split())
print(arr[x+y][y])
