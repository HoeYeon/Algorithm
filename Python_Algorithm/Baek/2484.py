import collections

maxx = -1
for i in range(int(input())):
    d = dict(collections.Counter(list(map(int, input().split()))))
    key = list(d.keys())
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    for k, v in d:
        if v == 4:
            maxx = max(maxx,50000+k*5000)
            break
        elif v == 3:
            maxx = max(maxx,10000+k*1000)
            break
        elif v == 2 and len(d) == 2:
            maxx = max(maxx,2000+sum(key)*500)
            break
        elif v == 2:
            maxx = max(maxx,1000 + k*100)
            break
        elif v == 1:
            maxx = max(maxx, k*100)
print(maxx)
