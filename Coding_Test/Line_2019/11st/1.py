def change(n,x):
    s=''
    while n>0:
        n,r  = divmod(n,x)
        if(r>9):
            r = chr(ord('a')+r-10)
        s = str(r)+s
    return s
N = 10
result = -1
ans = -1
for i in range(2,11):
    num = change(N,i)
    tmp = 1
    for j in num:
        if j != '0':
            tmp *= int(j)
    if tmp >= result:
        ans = i
        result = tmp
print(ans,result)
