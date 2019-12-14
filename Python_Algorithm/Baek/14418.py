def combi(li1, li2):
    tmp = []
    if li1[0] == li2[0]:
        tmp.append([li1[0], li1[1]+li2[1]])
    if li1[0] == li2[1]:
        tmp.append([li1[0], li1[1]+li2[0]])
    if li1[1] == li2[0]:
        tmp.append([li1[1], li1[0]+li2[1]])
    if li1[1] == li2[1]:
        tmp.append([li1[1], li1[0]+li2[0]])
    return tmp

li = [list(map(int, input().split())) for i in range(3)]
check = False
for i in range(2):
    for j in range(i+1, len(li)):
        s = combi(li[i], li[j])
        cmp = li[len(li)-(i+j)]
        for k in s:
            for p in combi(cmp,k):
                if p[0] == p[1]:
                    check = True
print('YES') if check else print('NO')
