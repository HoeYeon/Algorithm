N = int(input())
li = sorted(list(map(int,input().split())))
if li[0] != 1:
    print(1)
else:
    s = 1
    for i in li[1:]:
        if s+1 < i:
            break
        s += i
    print(s+1)
