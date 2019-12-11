for i in range(int(input())):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    dis = ((x1-x2)**2 + (y1-y2)**2)**(0.5)
    if x1 == x2 and y1 == y2:
        print(-1 if r1 == r2 else 0)
    elif dis > r1+r2:
        print(0)
    elif dis == r1+r2:
        print(1)
    elif dis < r1+r2:
        if dis + min(r1,r2) < max(r1,r2):
            print(0)
        elif dis+min(r1,r2) == max(r1,r2):
            print(1)
        else:
            print(2)
