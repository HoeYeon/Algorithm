def GCD(a,b): return GCD(b,a%b) if b else a
def LCM(a,b): return a*b//GCD(a,b)

N,M = map(int,input().split())
time = [0 for i in range(M+1)]
li = list(set([int(input()) for i in range(N)]))
for i in li:
    for j in range(0,M+1,i):
        time[j] = 1
print(sum(time)-1)