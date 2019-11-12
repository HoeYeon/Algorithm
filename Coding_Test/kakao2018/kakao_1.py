'''li = [1,2,3,4,5]
for i in range(len(li)-1,-1,-1):
    print(li[i])'''
def getnum(num):
    li = []
    while num > 0:
        li.append(num%10)
        num //= 10
    return li
def combine(li):
    num = 0
    for i in range(len(li)-1,-1,-1):
        num += (pow(10,len(li)-1-i) * li[i])
    return num
nn = int(input())
mmax = getnum(nn)
mmin = getnum(nn)
mmax.reverse()
mmin.reverse()
temp = 9
for i in mmax:
    if i == 9:
        continue
    else:
        temp = i
        break
for i in range(len(mmax)):
    if mmax[i] == temp:
        mmax[i] = 9
if mmin[0] != 1:
    temp = mmin[0]
    for i in range(len(mmin)):
        if mmin[i] == temp:
            mmin[i] = 1
else:
    temp = 0
    for i in range(1,len(mmin)):
        if mmin[i] == 0 and mmin[i] == 1:
            continue
        else:
            temp = mmin[i]
            break
    for i in range(1,len(mmin)):
        if mmin[i] == temp:
            mmin[i] = 0
print(mmax,mmin)
mmax = combine(mmax)
mmin = combine(mmin)
print(mmax,mmin)
