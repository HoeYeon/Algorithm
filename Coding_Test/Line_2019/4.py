n = int(input())
li = list(map(int,input().split(' ')))
result = 1
cnt = 1
for i in li:
    if i == 1:
        result = max(result,(cnt//2))
        cnt = 1
    else:
        cnt += 1
print(result)
