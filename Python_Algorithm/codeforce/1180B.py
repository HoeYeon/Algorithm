n = int(input())
li = list(map(int,input().split(' ')))
if n==1 and li[0] == 0:
    print(*li)
else:
    result = list(map(lambda x: -x-1 if x>=0 else x,li))
    #odd
    if n %2 == 1:
        idx = result.index(min(result))
        result[idx] = -result[idx] -1


    print(*result)
