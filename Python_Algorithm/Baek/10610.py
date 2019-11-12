S = input()
li = list(map(int,S))
if '0' not in S:
    print('-1')
else:
    if sum(li) % 3 != 0:
        print('-1')
    else:
        li = sorted(li,reverse=True)
        s = ''.join(str(e) for e in li)
        print(s)
