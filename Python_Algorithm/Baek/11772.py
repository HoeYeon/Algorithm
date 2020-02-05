result = 0
for i in range(int(input())):
    num = input()
    a,b = int(num[:-1]),int(num[-1])
    result += a**b
print(result)