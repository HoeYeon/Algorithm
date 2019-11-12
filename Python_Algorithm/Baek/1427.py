temp = int(input())
num = []
a=''
while temp >= 1:
    num.append(int(temp%10))
    temp = temp/10
num.sort()
num.reverse()
for i in num:
    a = a+str(i)
print(a)
