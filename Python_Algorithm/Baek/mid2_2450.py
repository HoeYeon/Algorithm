import itertools

N = int(input())
li = list(map(int,input().split()))
arr = list(map(list,itertools.permutations([1,2,3])))
num_c = [li.count(i+1) for i in range(3)]
ans = 9999999999
for i in arr:
    count = [[0 for j in range(3)] for i in range(3)]
    for k in range(len(li)):
        if k < num_c[i[0]-1]:
            if li[k] != i[0]:
                count[i[0]-1][li[k]-1] += 1
        elif k < num_c[i[0]-1]+num_c[i[1]-1]:
            if li[k] != i[1]:
                count[i[1]-1][li[k]-1] += 1
        else:
            if li[k] != i[2]:
                count[i[2]-1][li[k]-1] += 1
    result = min(count[0][1],count[1][0])
    result += max(count[2][1],count[1][2])
    result += max(count[0][2],count[2][0])
    ans = min(result,ans)
print(ans)
