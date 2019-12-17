arr = [5**i for i in range(1,14)]
arr2 = [2**i for i in range(1,35)]
n,m = map(int,input().split())
result = 0
for i in arr:
    result += n//i
    result -= m//i
    result -= (n-m)//i
result2 = 0
for j in arr2:
    result2 += n//j
    result2 -= m//j
    result2 -= (n-m)//j
print(min(result2,result))
