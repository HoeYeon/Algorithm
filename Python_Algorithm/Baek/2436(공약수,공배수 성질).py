def GCD(a,b): return GCD(b,a%b) if b else a
def LCM(a,b): return a*b//GCD(a,b)

a,b = map(int,input().split())
val = 1
f = b//a
for i in range(2,int(f**0.5)+1):
    if f%i == 0 and GCD(i,f//i) == 1:
        val = i
print(a*val,a*(f//val))
