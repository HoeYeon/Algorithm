n = int(input())
li = [0 for i in range(151)]
for i in range(n):
    a,b = map(int,input().split(' '))
    for i in range(a,b):
        li[i] += 1
print(max(li))
