import itertools

li = list(input().split(' '))
k = int(input())
ans = list(map(''.join, itertools.permutations(li)))
print(sorted(ans)[k-1])
print(ans)
