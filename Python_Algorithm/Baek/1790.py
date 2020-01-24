from math import ceil
N,K = map(int,input().split())
numcount,numlen = 9,1
tot = 0

while K > numcount*numlen:
    tot += numcount
    K -= numcount*numlen
    numcount *= 10
    numlen += 1
tot += ceil(K/numlen)
tmp = K % numlen
result = -1 if tot > N else int(str(tot)[tmp-1])
print(result)