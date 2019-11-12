n = int(input())
name = [input() for i in range(n)]
print(name)
q = int(input())
query = [input() for i in range(q)]
sum = [0 for i in range(q)]
for i in range(len(query)):
    for j in name:
        check = False
        if len(j) < len(query[i]):
            continue
        for k in range(len(query[i])):
            if query[i][k] != j[k]:
                break
            if k == len(query[i]) -1 and query[i][k] == j[k]:
                check= True
        if check and len(j) > len(query[i]):
            sum[i] += 1
print(sum)
