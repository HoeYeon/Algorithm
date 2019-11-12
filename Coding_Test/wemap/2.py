li = [0 for i in range(10000)]
count = 0
for i in range(1,10):
    for j in range(10):
        j = '' if j == 0 else str(j)
        for k in range(10):
            k = '' if k ==0 else str(k)
            for p in range(10):
                p = '' if p==0 else str(p)
                s = str(i)+j+k+p
                li[int(s)] = count
                count += 1
                if k == '':
                    break
            if j == '':
                break
print(li[int(input())])
