print(ord('z'))
#a == 97
#z == 122
#* == 42

s = input()
x = input()
check = False
if len(x) > len(s):
    print(-1)
elif x == s:
    print(0)
for i in range(len(s) - len(x)+1):
    for j in range(len(x)):
        if x[j] == '*' or x[j] == s[i+j]:
            if j == len(x)-1:
                check = True
                break
            else:
                continue
        else:
            break
    if check == True:
        break
if check == True:
    print(i)
else:
    print(-1)
