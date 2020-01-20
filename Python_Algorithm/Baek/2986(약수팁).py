N = int(input())
k = 1
for i in range(2,int(N**0.5)+1):
    if N%i == 0:
        k = N//i
        break
print(N-k)