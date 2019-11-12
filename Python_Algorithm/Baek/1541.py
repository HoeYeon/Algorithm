li = input().split('-')
result = 0
result += sum(list(map(int,li[0].split('+'))))
for i in range(1,len(li)):
    result -= sum(list(map(int,li[i].split('+'))))
print(result)
