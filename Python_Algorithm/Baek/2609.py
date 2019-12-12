def GCD(a,b): return GCD(b,a%b) if b else a
def LCM(a,b): return a*b//GCD(a,b)
a,b = map(int,input().split())
print(GCD(a,b),LCM(a,b))
