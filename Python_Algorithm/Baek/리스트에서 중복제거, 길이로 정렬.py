### 이게 원본
'''li = [set([]) for i in range(51)]
for i in range(int(input())):
    a = input()
    li[len(a)].add(a)
li2 = []
for i in range(51):
    a= list(li[i])
    a.sort()
    li2.append(a)
for i in li2:
    if len(i)>0:
        print('\n'.join(map(str,i)))'''
li =[]
for i in range(int(input())):
    a = input()
    li.append(a)
li = sorted(list(set(li))) # 중복제거
li.sort(key=len) #길이를 key로 해서 sort
print('\n'.join(li)
