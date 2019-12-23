def binsearch(start,end,k):
    mid = (start+end)//2
    if start > end:
        print(0)
        return
    elif li[mid] == k:
        print(1)
        return
    else:
        binsearch(start,mid-1,k) if k < li[mid] else binsearch(mid+1,end,k)


N = int(input())
li = sorted(list(map(int, input().split())))
M = int(input())
for i in list(map(int,input().split())):
    binsearch(0,N-1,i)
