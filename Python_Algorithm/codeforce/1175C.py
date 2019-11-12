for _ in range(int(input())):
    n,k = map(int,input().split(' '))
    a_li = list(map(int,input().split(' ')))
    if k == 0:
        print(a_li[0])
    else:
        mid = (a_li[k-1] + a_li[k])//2
        print(mid)
