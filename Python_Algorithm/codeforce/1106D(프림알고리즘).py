from heapq import *

n,m = map(int,input().split(' '))
li = [[] for i in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split(' '))
    li[u].append(v)
    li[v].append(u)
    
ins = [1]
ard = set()
while ins:
	u = heappop(ins)
	if u not in ard:
		print(u,end=' ')
		ard.add(u)
		for j in li[u]:
			heappush(ins, j)
