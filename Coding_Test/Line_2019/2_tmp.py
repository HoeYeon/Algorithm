tmp = '123'

li = []
check = [0 for i in range(3)]
def permute(s,c,cc):
    if c == len(tmp):
        li.append(s)
        return
    for i in range(3):
        if cc[i] == 0:
            cc[i] = 1
            permute(s+tmp[i],c+1,cc)
            cc[i] = 0
permute('',0,check)
print(li)
