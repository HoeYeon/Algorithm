import sys
 
input = sys.stdin.readline
 
N = int(input())
li = list(map(int,input().split()))
check = [1 for i in range(N+1)]
dup = [1 for i in range(N+1)]
for i in range(len(li)):
    ## fromgo
    if li[i] == 0:
        dup[i+1] += 1
    ## togo
    else:
        dup[li[i]] -= 1
        check[li[i]] = 0
dup2 = [i for i in range(1,len(dup)) if dup[i] == 2]
toGo = dup2[:]
fromGo = dup2[:]
for i in range(len(li)):
    if li[i] == 0 and dup[i+1] != 2:
        fromGo.append(i+1)
for i in range(1,len(check)):
    if check[i]&1 and dup[i] != 2:
        toGo.append(i)
for i in range(len(fromGo)):
    li[fromGo[i]-1] = toGo[(i+1)%len(toGo)]
result = list(map(str,li))
print(' '.join(result))