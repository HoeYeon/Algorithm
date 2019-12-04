N = int(input())
li = [list(map(int,input().split())) for i in range(N)]
result = []
for j in sorted(li):
    idx = len(result)-1
    while idx != -1 and result[idx] >= j[1]:
        idx -= 1
    if idx == len(result)-1:
        result.append(j[1])
    else:
        result[idx+1] = j[1]
print(N- len(result))
