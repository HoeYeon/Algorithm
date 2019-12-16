def GCD(a,b): return GCD(b,a%b) if b else a

n = int(input())
li = list(map(int, input().split()))
result = ''
for i in range(1,len(li)):
    tmp = GCD(li[0],li[i])
    result += str(li[0]//tmp) + '/' + str(li[i]//tmp) +'\n'
print(result)
