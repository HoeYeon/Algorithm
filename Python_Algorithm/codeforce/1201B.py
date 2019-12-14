n = int(input())
li = list(map(int,input().split(' ')))
s = sum(li)
if(s % 2 == 1):
    print('NO')
else:
    if len(li) %2 == 1:
        if max(li) > sum(li) - max(li):
            print('NO')
        else:
            print('YES') if sum(li) >= len(li)+1 else print('NO')
    else:
        if max(li) > sum(li) - max(li):
            print('NO')
        else:
            print('YES') if sum(li) >= len(li) else print('NO')
