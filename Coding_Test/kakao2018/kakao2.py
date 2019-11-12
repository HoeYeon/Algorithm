n = int(input())
A = [[0 for i in range(26)] for i in range(n)]
B = [[0 for i in range(26)] for i in range(n)]
for i in range(n):
    temp = input()
    if len(temp) > 1:
        for j in temp:
            A[i][97-ord(j)] += 1
    else:
        A[i][97-ord(temp)] += 1
n = int(input())
for i in range(n):
    temp = input()
    if len(temp) > 1:
        for j in temp:
            B[i][97-ord(j)] += 1
    else:
        B[i][97-ord(temp)] += 1
for i in range(n):
    result = 0
    if sum(A[i]) != sum(B[i]):
        print(-1)
    else:
        for j in range(26):
            result += abs(A[i][j] - B[i][j])
        print(result//2)
