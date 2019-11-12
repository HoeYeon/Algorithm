n,thr = input().split(' ')
li = []
for i in range(int(n)):
    a,b = input().split(' ')
    li.append([int(a),b])
print(li)
max_row = max(li)[0]
max_col = max_row*2 -1
num_list = [[0,1,2,3,4,5],[1,2],[0,1,3,4,6],[0,1,2,3,6],[1,2,5,6],[0,2,3,5,6],
    [2,3,4,5,6],[0,1,2],[0,1,2,3,4,5,6],[0,1,2,5,6],[0,1,2,3,4,5]]

for i in range(max_col):
    for j in range(int(n)):
        row = li[j][0]
        s = li[j][1]
        base = 0
        for p in s:
            check = False
            num = int(p)
            for k in range(row):
                col = row*2 -1
                if col-1 < i and thr == 'TOP':
                    print('.',end='')
                elif i < (max_col - col) and thr == 'BOTTOM':
                    print('.',end='')
                    check = True
                elif thr == 'MIDDLE' and (i<(max_col - col)//2 or i>(max_col-col)//2+col-1):
                    print('.',end='')
                    check = True
                else:
                    if thr == 'MIDDLE':
                        base = (max_col-col)//2
                    if thr == 'BOTTOM':
                        base = (max_col-col)
                    if 0 in num_list[num] and i == base:
                        print('#',end='')
                        continue
                    if 6 in num_list[num] and i == col//2 + base:
                        print('#',end='')
                        continue
                    if 3 in num_list[num] and i == col-1 +base:
                        print('#',end='')
                        continue
                    if 5 in num_list[num] and i <= col//2+base and k == 0:
                        print('#',end='')
                    elif 1 in num_list[num] and i <= col//2+base and k == row-1:
                        print('#',end='')
                    elif 4 in num_list[num] and i >= col//2+base and k == 0:
                        print('#',end='')
                    elif 2 in num_list[num] and i >= col//2+base and k == row-1:
                        print('#',end='')
                    else:
                        print('.',end='')
            print(' ',end='')
        print(' ',end='')
    print()
