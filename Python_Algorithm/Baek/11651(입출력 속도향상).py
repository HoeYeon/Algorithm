import sys

input = sys.stdin.readline
## 주의 print는 하나의 string만 받을 수 있으므로 여러개 출력하려면 아래처럼 포맷팅 해야됨
## print(a,b) 이런식으로 못씀
print = sys.stdout.write
li = []
for i in range(int(input())):
    a,b = map(int,input().split())
    li.append([b,a])
li.sort()
for i in li:
    print("%d %d\n"% (i[1],i[0]))
