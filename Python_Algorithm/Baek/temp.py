from math import *
n,k = map(int,input().split(' '))
num = list(map(int,input().split(' ')))
d = [round(100/n*i) for i in range(1,n+1)]
size = k
li = num[0:size]
cmp = [0 for i in range(size)]
count = d[0]
result = 0
while count != 100:
    if len(li) < k:
        li.append(num[size])
        cmp.append(0)
        size += 1
    for i in range(len(li)):
        cmp[i] += 1
    for i in range(len(li)):
        if cmp[i] == count and count != 100:
            print(li[i])
            result += 1
    if li[i] == cmp[i]:
        del li[i]
        del cmp[i]
        count = d[d.index(count)+1]
print(result)
