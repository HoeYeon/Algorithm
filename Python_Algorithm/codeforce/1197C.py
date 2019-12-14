n,k = map(int,input().split(' '))
li = list(map(int,input().split(' ')))

mi = [li[i+1] - li[i] for i in range(len(li)-1)]
mi.sort()
print(sum(mi[:n-k]))
