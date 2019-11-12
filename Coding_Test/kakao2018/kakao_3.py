n = int(input())
ee = [int(input()) for i in range(n)]
t = int(input())
m = int(input())
team = []
lm = rm = m
for i in range(t):
    if len(ee) < lm or len(ee) < rm:
        team.append(max(ee))
        ee[ee.index(max(ee))] = -1
    else:
        lmax = max(ee[0:lm])
        rmax = max(ee[-rm:len(ee)])
        if lmax > rmax:
            team.append(lmax)

            del ee[ee.index(lmax)]
        else:
            team.append(rmax)
            idx = len(ee) - m - ee[-m:len(ee)].index(rmax)
            del ee[idx]
print(team)
