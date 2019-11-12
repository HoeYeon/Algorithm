m,c = map(int,input().split(' '))
li = [int(input()) for i in range(m)]
c_li = [0 for i in range(c)]
for i in range(c):
    c_li[i] = li[i]

for i in range(c,m):
    c_li.sort()
    c_li[0] += li[i]
print(max(c_li))
