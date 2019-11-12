N,M = map(int,input().split(' '))
a = set([input() for i in range(N)])
b = set([input() for i in range(M)])
c = list(a&b)
c. sort()
print(len(c))
for i in range(len(c)):
    print(c[i])
