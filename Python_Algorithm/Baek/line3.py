'''6
id name occupation
5 Brown Accountant
2 Cony Programmer
3 Sally Doctor
1 James Singer
4 Moon Dancer
7
id city zip
2 Seoul 10008
7 Busan 40002
5 Gwangju 20009
6 Daegu 30008
3 Seoul 40005
1 Seoul 50006'''
N = int(input())
col= list(input().split(' '))
li = []
for i in range(N-1):
    a = list(input().split(' '))
    li.append(a)
N2 = int(input())
col2 = list(input().split(' '))
li2 = []
for i in range(N2-1):
    a = list(input().split(' '))
    li2.append(a)
li3 =[]
col = col + col2[1:len(col2)]
li.sort()
li2.sort()
for i in range(N-1):
    li3.append(li[i])
    check = 0
    for j in li2:
        if li[i][0] in j:
            check = 1
            break
    if check == 1:
        li3[-1] = li3[-1] + j[1:len(li2)]
    else:
        li4 = ['NULL' for k in range(len(li2[i]))]
        li3[-1] = li3[-1] + li4[1:len(li4)]

for i in col:
    print(i,end=' ')
print()
for i in li3:
    for j in i:
        print(j,end=' ')
    print()
