n = int(input())
weight = [0 for i in range(150002)]
li = list(map(int,input().split(' ')))
cnt = 0
weight[0] = 1
li.sort()
for i in li:
    if weight[i-1] == 0:
        weight[i-1] = 1
        cnt += 1
    else:
        if weight[i] == 0:
            weight[i] = 1
            cnt += 1
        elif weight[i+1] == 0:
            weight[i+1] = 1
            cnt += 1
print(cnt)
