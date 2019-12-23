from collections import Counter

input()
li = Counter(list(map(int,input().split())))
input()
re = ''
for i in list(map(int,input().split())):
    re += str(li[i]) + ' '
print(re)
