arr = [-1 for i in range(91)]
arr[0] = 0
arr[1] = 1

for i in range(2,91):
    arr[i] = arr[i-1] + arr[i-2]
print(arr[int(input())])
