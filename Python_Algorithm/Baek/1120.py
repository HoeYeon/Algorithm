a, b = input().split(' ')
if len(b) > len(a):
    a, b = b, a
result = 0
for i in range(0,len(a)-len(b)+1):
    count = 0
    for j in range(0, len(b)):
        if a[i+j] == b[j]:
            count += 1
    result = max(result,count)
print(len(b) - result)
