import re

p = re.compile('<[\w\s]*>')
ex = input()
li2 = p.findall(ex)
li = [i.span() for i in p.finditer(ex)]
result = ''
for i in range(0, len(li)):
    if i == 0:
        tmp = ex[:li[i][0]].split()
        tmp = [i[::-1] for i in tmp]
        if len(tmp) != 0:
            tmp = ' '.join(tmp)
            result += str(tmp)
    result += li2[i]
    if i == len(li)-1:
        tmp = ex[li[i][1]:].split()
        tmp = [i[::-1] for i in tmp]
        if len(tmp) != 0:
            tmp = ' '.join(tmp)
            result += str(tmp)
        continue
    tmp = ex[li[i][1]:li[i+1][0]].split()
    tmp = [i[::-1] for i in tmp]
    if len(tmp) != 0:
        tmp = ' '.join(tmp)
        result += str(tmp)
if len(li) == 0:
    ex = ex.split()
    result = [i[::-1] for i in ex]
    result = ' '.join(result)
print(result)
