w = int(input())
n = int(input())
li = sorted(list(map(int,input().split())),reverse=True)
check = [0 for i in range(n)]
if li[0] > w:
    print(-1)
    exit(0)
count = 0
while True:
    s = 0
    if all(check):
        break
    for i in range(n):
        if li[i] + s <= w and check[i] == 0:
            s += li[i]
            check[i] = 1
    count += 1
print(count)
