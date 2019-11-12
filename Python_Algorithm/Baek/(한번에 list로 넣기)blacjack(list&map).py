N,M = map(int, input().split(' '))
li = list(map(int,input().split(' ')))
s = 300001
for i in range(0,N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if M - (li[i] + li[j] + li[k]) < abs(M -s) and M - (li[i] + li[j] + li[k]) >= 0:
                s = li[i] + li[j] + li[k]
print(s)
