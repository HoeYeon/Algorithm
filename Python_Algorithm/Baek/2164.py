n = int(input())
d = list(range(n))
i = False
for x in d:
    if i:
        d.append(x)
    i = not i
print(x + 1)
