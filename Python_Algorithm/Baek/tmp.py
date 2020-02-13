li = [[4,5,6],[1,2,3],[7,8]]
print(li)
print(sorted(li,key=lambda x: len(x)))

def check(arr,cmp):
    for i in arr:
        print('i:',i)
        print('cmp:',cmp)
        while len(i) > 0:
            if i[0][0] + i[0][1] < cmp[0]:
                i.pop(0)
            else:
                i[0] = [cmp[0],i[0][0]+i[0][1] - cmp[0]]
                break
    


time = [[1,3],[6,5],[7,2],[10,9],[12,3]]
li = [[],[]]
for i in time:
    print('li: ',li)
    check(li,i)
    li = sorted(li,key=lambda x: len(x))
    li[0].append(i)
print(li)