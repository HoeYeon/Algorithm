'''def fact(n):
    return 1 if n == 1 or n == 0 else n*fact(n-1)
N = int(input()) - 1
s = 0
for i in range(N//2+1):
    one_num = N - i*2
    s += fact(one_num+i)//(fact(one_num)*fact(i))
print(s)
'''
arr = [[0 for j in range(60)] for i in range(60)]
for i in range(60):
    for j in range(i+1):
        arr[i][j] = 1 if i==0 or j ==0 else arr[i-1][j] + arr[i-1][j-1]
N = int(input())-1
s = 0
for i in range(N//2+1):
    one_num = N - i*2
    s += arr[one_num+i][i]
print(s)
