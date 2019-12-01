A = input()
B = input()
arr = [[0 for i in range(len(A)+1)] for j in range(len(B)+1)]

print(arr)
for i in range(len(B)):
    for j in range(len(A)):
        if B[i] == A[j]:
            # 2개가 같다면 좌 대각선 + 1
            arr[i+1][j+1] = arr[i+1-1][j+1-1]+1
        else:
            # 2개가 다르다면 좌측 or 상단중에 큰 값을 가져온다.
            arr[i+1][j+1] = max(arr[i+1-1][j+1],arr[i+1][j+1-1])
print(arr[len(B)][len(A)])
for i in arr:
    print(i)
