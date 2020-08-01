start, pointer = input().split(";")
pointer = pointer.split()
t = pointer[int(start)]
q = []
while t != "1":
    q.append([t, pointer[int(start) + 1]])
    start = pointer[int(start) + 1]
    t = pointer[int(start)]
q.append([t, pointer[int(start) + 1]])
ans = [0 for i in range(8)]
tmp = 2
idx = 0
for i in q:
    if i[0] == "0":
        ans[idx] = 0
        ans[idx + 1] = tmp
        tmp += 2
        idx += 2
    else:
        ans[idx] = 1
        ans[idx + 1] = int(i[1])
print("0;", " ".join(map(str, ans)))

