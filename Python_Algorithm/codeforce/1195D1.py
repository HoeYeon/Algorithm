n = int(input())
li = list(input().split(' '))

length = len(li[0])
result = 0
for i in range(n):
    #1,2,3
    for j in range(length):
        result += (10**(2*j)) * int(li[i][length-j-1])*n
        result += (10**((2*j+1))) * int(li[i][length-j-1])*n
print(result%998244353)
#print(sum(re)%998244353)
